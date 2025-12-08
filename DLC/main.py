import os
import sys
import time
import tiles
import story
from menu import Menu
from mapper import display, animate, stage
import controls
from story import level_loading_screen, world_loading_screen


menu = Menu("main")

moves = ""
reset_story = False
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def run_input(indiv_input: str):
    "handles the inputs of player"
    global curr_stage, reset_story
    #movement
    if indiv_input in controls.movement_keybinds:
        for char in curr_stage.characters:
            char.move(controls.movement_keybinds[indiv_input.lower()])
            if char.dead:
                story.death_sec()
                char.dead = False
                if menu.storymode:
                    reset_story = True
                    return
                else:
                    menu.prev = "main"
                    menu.main_menu()
                    curr_stage = menu.curr_stage
            
    #ui
    elif indiv_input in controls.ui_keybinds:
        key = getattr(menu, controls.ui_keybinds[indiv_input.lower()])
        key()
        curr_stage = menu.curr_stage

    #player actions
    elif indiv_input in controls.player_action_keybinds:
        for char in curr_stage.characters:
            if not curr_stage.inventory and char.curr_tile is not None and "manual_pickup" in tiles.tile_object_tags[char.curr_tile]:
                curr_stage.inventory = char.curr_tile
                char.curr_tile = None

args = len(sys.argv)

if args == 2: # shroom_raider.py map.txt
    menu.curr_stage = stage(sys.argv[1])
    menu.curr_stage.start()
    curr_stage = menu.curr_stage
    
elif args == 4: # shroom_raider.py map.txt "asdasd" output.txt
    menu.curr_stage = stage(sys.argv[1])
    menu.curr_stage.start()
    curr_stage = menu.curr_stage

    won = False
    for indiv_input in sys.argv[2].lower():
        run_input(indiv_input)
        if curr_stage.score >= curr_stage.score_req:
            won = True
            break
    try:
        output_file = open(f"{sys.argv[3]}", "w")
        with output_file as file:
            if won:
                file.write("CLEAR\n")
            else:
                file.write("NO CLEAR\n")
            file.write(str(curr_stage.y) + " " + str(curr_stage.x) + "\n")
            file.write(display(curr_stage, True))
        print("it fucking worked")
    except FileNotFoundError:
        print(f"Error: Output file {sys.argv[3]} not found.") 
    exit()
    


def run_game(story_status=False):
    global moves
    clear()
    print(display(curr_stage, False))
    print(f"\N{mushroom}: {curr_stage.score}")
    menu.prev = "in_game"
    # Pickup prompt
    if not curr_stage.inventory:
        print("Currently holding NOTHING")
        for char in curr_stage.characters:
            if char.curr_tile and "manual_pickup" in tiles.tile_object_tags[char.curr_tile]:
                print(f"Press P to pick up [{tiles.translate_tiles[char.curr_tile]}]")
                break
    else:
        print(f"Currently holding [{tiles.translate_tiles[curr_stage.inventory]}]")

    #move player
    for indiv_input in input("> ").lower():
        moves += indiv_input
        clear()
        run_input(indiv_input)
        animate(curr_stage, 0.1)
        print(f"\N{mushroom}: {curr_stage.score}")
        if curr_stage.score >= curr_stage.score_req:
            if not story_status:
                menu.win_screen2()
                return
            else:
                return True
        curr_stage.update()
    menu.prev = "in_game"


story.open_sec()
while True:
    menu.main_menu()
    curr_stage = menu.curr_stage

    if menu.storymode:
        reset_story = False
        level_anim = True
        world_list = tuple(list(os.walk("maps"))[0][1])
        for world in world_list:
            clear()
            all_levels = os.listdir(f"maps/{world}")
            world_loading_screen(world)
            for i, level in enumerate(sorted(all_levels, key=len)):
                clear()
                menu.curr_stage = stage(f"{world}/{level}")
                menu.prev_map = f"{world}/{level}"
                menu.curr_stage.start()
                curr_stage = menu.curr_stage
                level_loading_screen(i + 1, len(all_levels), level_anim)
                if level_anim:
                    level_anim = False  
                while True: 
                    if reset_story:
                        break
                    if run_game(True):
                        break
                if reset_story:
                    break
            if reset_story:
                break
        if reset_story:
            continue
        menu.win_screen()
    else:
        while True:
            run_game()
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    
        