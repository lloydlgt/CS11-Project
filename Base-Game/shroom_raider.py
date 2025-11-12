import os
import time
import tiles
from argparse import ArgumentParser
from menu import Menu, win_screen
from mapper import stage, display
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

    # Player UI
    elif indiv_input in controls.ui_keybinds:
        key = getattr(menu, controls.ui_keybinds[indiv_input.lower()])
        key()
        curr_stage = menu.curr_stage

    else:
        pass

parser = ArgumentParser()
parser.add_argument("stage_file", type=str, nargs="?", default="default.txt")
parser.add_argument("string_of_moves", type=str, nargs="?", default="")
parser.add_argument("output_file", type=str, nargs="?", default=None)
args = parser.parse_args()
print(args.stage_file, args.string_of_moves, args.output_file)
time.sleep(1)


# Map booting
menu.curr_stage = stage(args.stage_file)
menu.prev_map = args.stage_file
curr_stage = menu.curr_stage
menu.curr_stage.start()


# If user enters an output file
if args.output_file:
    won = False
    for indiv_input in args.string_of_moves.lower():
        run_input(indiv_input)
        if curr_stage.score >= curr_stage.score_req:
            won = True
            break
    try:
        with open(args.output_file, "w") as file:
            if won:
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
        clear()
        run_input(indiv_input)
        print(display(curr_stage, False))
        print(f"\N{mushroom}: {curr_stage.score}")

        # Win condition
        if curr_stage.score >= curr_stage.score_req:
            clear()
            print(display(curr_stage, False))
            print(f"\N{mushroom} collected: {curr_stage.score}")
            win_screen()
            exit()
