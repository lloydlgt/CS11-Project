import os
import tiles
from argparse import ArgumentParser
from mapper import stage, display
import controls

# Clears the user terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Processes every user movement/input

# Accepting user command-line arguments
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

    
if args.output_file != None:
    """
    If the user enters an output file,
    Run the string of moves,
    Write current stage in the output file,
    Terminate the program
    """

    win = False
    
    for indiv_input in args.string_of_moves.lower():
        run_input(indiv_input, curr_stage)
        if curr_stage.score >= curr_stage.score_req:
            win = True
            break

    try:
        with open(args.output_file, "w") as file:
            if win: file.write("CLEAR\n")
            else: file.write("NO CLEAR\n")
            file.write(str(curr_stage.y) + " " + str(curr_stage.x) + "\n")
            file.write(display(curr_stage, True))
        print(f"Successfully output to {args.output_file}.")
    except FileNotFoundError:
        print(f"Error: Output file {args.output_file} not found.") 
        
    exit()
else:
    pass

def reset():
    global curr_stage, prev_map
    "resets the map"
    curr_stage = stage(prev_map)
    curr_stage.start()

def death_screen():
    global curr_stage
    os.system("cls" if os.name == "nt" else "clear")
    print(display(curr_stage, False))
    print(f"\N{mushroom} collected: {curr_stage.score}")
    print("Game Over! Try again next time.")
    exit()

def win_screen():
    "The win screen once all mushroom has been collected"
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

# "Main" or in-game part of the game
def game_running():
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
        for indiv_input in input("> ").lower():
            validated_input = curr_stage.character.run_input(indiv_input)
            if not validated_input:
                break
            if validated_input == "reset":
                reset()
            if validated_input == "dead":
                death_screen()
            # If user has reached the win condition
            if curr_stage.score >= curr_stage.score_req:
                clear()
                print(display(curr_stage, False))
                print(f"\N{mushroom} collected: {curr_stage.score}")
                win_screen()
                exit()
        clear()
        print(display(curr_stage, False))
        print(f"\N{mushroom}: {curr_stage.score}")

if args.stage_file:
    game_running()