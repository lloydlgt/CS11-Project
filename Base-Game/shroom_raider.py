import os
import sys
import time
import tiles
from menu import Menu, win_screen
from mapper import stage, display
from player import character
import controls

menu = Menu()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def run_input(indiv_input: str):
    global curr_stage
    # Player movement
    if indiv_input in controls.movement_keybinds:
        for char in curr_stage.characters:
            char.move(controls.movement_keybinds[indiv_input.lower()])

    # Player interactions
    elif indiv_input in controls.player_action_keybinds:
        for char in curr_stage.characters:
            if not curr_stage.inventory and char.curr_tile and "manual_pickup" in tiles.tile_object_tags[char.curr_tile]:
                curr_stage.inventory = char.curr_tile
                char.curr_tile = None

    elif indiv_input in controls.ui_keybinds:
        key = getattr(menu, controls.ui_keybinds[indiv_input.lower()])
        key()
        curr_stage = menu.curr_stage


# Map booting
args = len(sys.argv)
if args == 1: # shroom_raider.py // Load default stage
    menu.curr_stage = stage("default.txt")
    menu.prev_map = "default.txt"
    curr_stage = menu.curr_stage
    menu.curr_stage.start()


elif args == 2: # shroom_raider.py map.txt // Load map input stage
    menu.curr_stage = stage(sys.argv[1])
    menu.prev_map = sys.argv[1]
    curr_stage = menu.curr_stage
    menu.curr_stage.start()

elif args == 4: # shroom_raider.py map.txt "wasd" output.txt // Load map input stage -> Run string of moves -> Write to output file
    menu.curr_stage = stage(sys.argv[1])
    menu.prev_map = sys.argv[1]
    curr_stage = menu.curr_stage
    menu.curr_stage.start()

    won = False
    for indiv_input in sys.argv[2].lower():
        run_input(indiv_input)
        if curr_stage.score >= curr_stage.score_req:
            won = True
            break
    try:
        with open(f"{sys.argv[3]}", "w") as file:
            if won:
                file.write("CLEAR\n")
            else:
                file.write("NO CLEAR\n")
            file.write(str(curr_stage.y) + " " + str(curr_stage.x) + "\n")
            file.write(display(curr_stage, True))
        print(f"Successfully output to {sys.argv[3]}.")
    except FileNotFoundError:
        print(f"Error: Output file {sys.argv[3]} not found.") 
    exit()
else:
    pass


# "Main"
while True:
    clear()

    # Terminal displays
    print(display(curr_stage, False))
    print(f"\N{mushroom}: {curr_stage.score}")

    # Pickup prompt
    if not curr_stage.inventory:
        print("Currently holding [ ]")
        for char in curr_stage.characters:
            if char.curr_tile and "manual_pickup" in tiles.tile_object_tags[char.curr_tile]:
                print(f"Press P to pick up [{tiles.translate_tiles[char.curr_tile]}]:")
                break
    else:
        print(f"Currently holding [{tiles.translate_tiles[curr_stage.inventory]}]")

    # Player movement
    for indiv_input in input("> ").lower():
        time.sleep(0.1)
        clear()
        run_input(indiv_input)
        print(display(curr_stage, False))
        print(f"\N{mushroom}: {curr_stage.score}")

        # Win condition
        if curr_stage.score >= curr_stage.score_req:
            win_screen()
    
    
    
