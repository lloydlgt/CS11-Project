import os
import tiles
import json
from argparse import ArgumentParser
from mapper import stage, display

MOVES_NUM = 0

def clear():
    """Clears the user terminal"""
    os.system("cls" if os.name == "nt" else "clear")

# Processes every user movement/input

# Accepting user command-line arguments
parser = ArgumentParser()
parser.add_argument("-f", "--stage_file", type=str, default="default.txt")
parser.add_argument("-m", "--string_of_moves", type=str, default="")
parser.add_argument("-o", "--output_file", type=str, default=None)
args = parser.parse_args()

# Map booting
curr_stage = stage(args.stage_file) # self.path only
prev_map = args.stage_file # saves txt file
curr_stage.start() 
    
if args.output_file is not None:
    """If the user enters an output file,
    Run the string of moves,
    Write current stage in the output file,
    Terminate the program
    """

    win = False
    
    for indiv_input in args.string_of_moves.lower():
        validated_input = curr_stage.character.run_input(indiv_input)
        if not validated_input:
            break
        if validated_input == "reset":
            curr_stage.reset()
        if validated_input == "dead":
            break
        if curr_stage.score >= curr_stage.score_req:
            win = True
            break

    try:
        with open(args.output_file, "w") as file:
            if win: 
                file.write("CLEAR\n")
            else: 
                file.write("NO CLEAR\n")
            file.write(str(curr_stage.y) + " " + str(curr_stage.x) + "\n")
            file.write(display(curr_stage, True))
        print(f"Successfully output to {args.output_file}.")
    except FileNotFoundError:
        print(f"Error: Output file {args.output_file} not found.") 
        
    exit()
else:
    pass

def death_screen():
    """death screen when the player reaches a tile with death_on_touch tag"""
    global curr_stage
    os.system("cls" if os.name == "nt" else "clear")
    print(display(curr_stage, False))
    print(f"\N{mushroom} collected: {curr_stage.score}")
    print("Game Over! Try again next time.")
    exit()

def win_screen():
    """The win screen once all mushroom has been collected"""
    print("Congrats, you've finished the game! have a cake :)")
    print("""                  
            /M/              .,-=;//;-
        .:/= ;MH/,    ,=/+%$XH@MM#@:
        -$##@+$###@H@MMM#######H:.    -/H#H
    .,H@H@ X######@ -H#####@+-     -+H###@X
    .,@##H;      +XM##M/,     =%@###@X;-
    X%-  :M##########$.    .:%M###@%:
    M##H,   +H@@@$/-.  ,;$M###@%,          --
    M####M=,,---,.-HHH####M$:          ,+@##
    @##################@/.         :%H##@$-
    M###############H,         ;HM##M$=
    #################.    .=$M##M$=
    ################H..;XM##M$=          .:++
    M###################@%=           =+@MH%
    @#################M/.         =+H#X%=
    =+M###############M,      ,/X#H+:,
    .;XM###########H=   ,/X#H+:;
        .=+HM#######M+/+HM@+=.
            ,:/XMM####H/.
        
    """)
    exit()

def game_running():
    """"Main" or in-game part of the game"""
    global MOVES_NUM
    name = input("what is your name? ")
    while True:
        clear()

        # Displays necessary game information on the terminal
        print(display(curr_stage, False))
        print(f"\N{mushroom}: {curr_stage.score}")

        # Prompts the user for pickup on an item tile and shows the current item holding
        if not curr_stage.inventory:
            print("Currently holding [ ]")
            if curr_stage.character.curr_tile and "manual_pickup" in tiles.tile_object_tags[curr_stage.character.curr_tile]:
                print(f"Press P to pick up [{tiles.translate_tiles[curr_stage.character.curr_tile]}]:")
        else:
            print(f"Currently holding [{tiles.translate_tiles[curr_stage.inventory]}]")
        
        # Player movement for each input
        moves = input("> ").lower()
        for indiv_input in moves:
            MOVES_NUM += 1
            validated_input = curr_stage.character.run_input(indiv_input)
            if not validated_input:
                break
            if validated_input == "reset":
                MOVES_NUM = 0
                curr_stage.reset()
            if validated_input == "dead":
                death_screen()
            # If user has reached the win condition
            if curr_stage.score >= curr_stage.score_req:
                clear()
                print(display(curr_stage, False))
                print(f"\N{mushroom} collected: {curr_stage.score}")

                stage_path = f"leaderboards\\l_{curr_stage.path[:-4]}.json"
                if not os.path.isfile(stage_path) or os.path.getsize(stage_path) == 0:
                    scores = {}
                else:
                    with open(stage_path, "r", encoding="utf-8") as leaderboard:
                        try:
                            scores = json.load(leaderboard)
                        except json.JSONDecodeError:
                            scores = {}
                            
                if name not in scores or MOVES_NUM <= scores[name]:
                    scores[name] = MOVES_NUM

                with open(stage_path, "w", encoding="utf-8") as leaderboard:
                    json.dump(scores, leaderboard, indent=4)
                win_screen()
        clear()
        print(display(curr_stage, False))
        print(f"\N{mushroom}: {curr_stage.score}")

game_running()


   
"""time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
print(
                                                                                            
                                                                                            
                                                                                            
                                    ░░░▓▓▓▓▒░░░                                               
                                ░▒██████████▓                                               
                                ░▒████▓▓█▓░▒▒░░░░░                                            
                                ░██▒░▒▒░▒▒▒▒▒░▒░                                             
                                ░░▒▓▓▒▒░░▒▒▒▒▒░░                                            
                                ░▒▒▒░░░░▒░▒▒░░░░░                                           
                                    ░▒▒██▓░▒▒▓▓▓▓▓▓▓░                                          
                                    ░▓▒▒░░▒▓▓▓▓▓▓▓▓▓▒░░                                       
                                    ░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░                                   
                    ░░░░░░░░░░░ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░                                
                    ░▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                               
                ░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░░                        
                ░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░                     
                ░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░                    
                ░░░░▒░░░░░░▒░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░                   
                ░░▒░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░                  
                ▒░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░                  
                ░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▒░                  
            ░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░                  
        ░░▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░                
        ░▓█▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▒░░░░░▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░               
        ░▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▒░░░░░░░░░░▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░              
        ░▓█▓▓▓▒▒▒▒▒▓██▓▓▓████▓▓▓▓▓▓▓▓▓█████▓░░░░▒▒░▒▒▒▒▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓░             
        ▒▓░▒▓▒░░░░░▒▒▒▒▒▓███████████████▓▓░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▓▓▓▓▓▓▒░░▒▒▒░▒░░▓▓░░            
        ░░▒▓▓▓▒░░░░░░░░░▒██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░      ░█▒▒░░░░░░▒░░▒░ ░▒▒░            
        ▒▓▒▓▓▓▓▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░      ░█▓░░░░░░░░░▒▒░░ ░░             
        ░▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▒▒▒░░░░░▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓█▓▓▓▓▓▓▓▓▓▒▒░░░▓█▓▒░░░░░░▒▒▓▒░                
        ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓░                  
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓░                    
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓░                     
    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                    
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                  
    ▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                 
    ▒█▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓                  
    ░█▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▓▓▓                  
    ▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░▒▓▓▓▓▒                  
    ░▓▓▓▓▓▓▓▓▓▒░░░░░░░░░▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▓▓░░                  
        ░▓▓▓▓▓▓▓▒░░░░░░░░░░░░░▒▒▒▓█▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓█▓░░░░░░░░                    
        ░░▓▓▓▓░░░░░░░░░░░░░░░░░▒▒▓███████████▒░░▓█████████████▓▒░░░░▒░░                      
            ░░▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▒░░░░  ░▒▒▓███████▓▒░░░░░░░░                        
            ░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▒░░░░░░░▒▒▒▒▒░    ░▒▒▒▒▒▒▒▒▒░░░░░░░░░                           
                            ░░░░░░░▒▒▒▒▒▒░    ░▒▒▒▒▒▒▒▒░░░░▒░░                              
                            ░░░░░░▒▒▒▒▒▒▒░    ░▒▒▒▒▒▒▒▒░░░░░░                               
                                ░░░░▒▒▒▒▒▒▒░░     ░▒▒▒▒▒▒▒▒░░░░░░                              
                            ░░░░░▒▒▒▒▒▒░        ░▒▒▒▒▒▒▒▒░░░░░░                             
                        ░░░░░░░░░▒▒▒▒▒▒░           ░▒▒▒▒▒▒▒░░░░░░░░                          
                        ░░░░░░░░░░▒▒▒▒▒▒░             ░▒▒▒▒▒▒▒▒░░░░░░░                         
                        ░░░░░░░░▒▒▒▒▒▒▒▒░              ░▒▒▒▒▒▒▒▒▒▒▒▒░▒░                        )
time.sleep(12)
"""
    
        
