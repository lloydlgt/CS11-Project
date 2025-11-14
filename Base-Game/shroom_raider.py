import os
import tiles
from argparse import ArgumentParser
from menu import Menu, win_screen
from mapper import stage, display
import controls

menu = Menu()

# Clears the user terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Processes every user movement/input
def run_input(indiv_input: str):
    """ Runs each individual input
    Args:
        indiv_input: Individual input
    """

    # Player movement
    if indiv_input in controls.movement_keybinds:
        menu.curr_stage.character.move(controls.movement_keybinds[indiv_input.lower()])

    # Player interactions
    elif indiv_input in controls.player_action_keybinds:
        if not menu.curr_stage.inventory and menu.curr_stage.character.curr_tile and "manual_pickup" in tiles.tile_object_tags[menu.curr_stage.character.curr_tile]:
            menu.curr_stage.inventory = menu.curr_stage.character.curr_tile
            menu.curr_stage.character.curr_tile = None

    # Player UI
    elif indiv_input in controls.ui_keybinds:
        key = getattr(menu, controls.ui_keybinds[indiv_input.lower()])
        key()
    else:
        pass

# Accepting user command-line arguments
parser = ArgumentParser()
parser.add_argument("stage_file", type=str, nargs="?", default="default.txt")
parser.add_argument("string_of_moves", type=str, nargs="?", default="")
parser.add_argument("output_file", type=str, nargs="?", default=None)
args = parser.parse_args()


# Map booting
menu.curr_stage = stage(args.stage_file) # self.path only
menu.prev_map = args.stage_file # saves txt file
menu.curr_stage.start() 


if args.output_file != None:
    """
    If the user enters an output file,
    Run the string of moves,
    Write current stage in the output file,
    Terminate the program
    """

    win = False
    
    for indiv_input in args.string_of_moves.lower():
        run_input(indiv_input)
        if menu.curr_stage.score >= menu.curr_stage.score_req:
            win = True
            break

    try:
        with open(args.output_file, "w") as file:
            if win: file.write("CLEAR\n")
            else: file.write("NO CLEAR\n")
            file.write(str(menu.curr_stage.y) + " " + str(menu.curr_stage.x) + "\n")
            file.write(display(menu.curr_stage, True))
        print(f"Successfully output to {args.output_file}.")
    except FileNotFoundError:
        print(f"Error: Output file {args.output_file} not found.") 
        
    exit()
else:
    pass


# "Main" or in-game part of the game
while True:
    clear()

    # Displays necessary game information on the terminal
    print(display(menu.curr_stage, False))
    print(f"\N{mushroom}: {menu.curr_stage.score}")

    # Prompts the user for pickup on an item tile and shows the current item holding
    if not menu.curr_stage.inventory:
        print("Currently holding [ ]")
        if menu.curr_stage.character.curr_tile and "manual_pickup" in tiles.tile_object_tags[menu.curr_stage.character.curr_tile]:
            print(f"Press P to pick up [{tiles.translate_tiles[menu.curr_stage.character.curr_tile]}]:")
    else:
        print(f"Currently holding [{tiles.translate_tiles[menu.curr_stage.inventory]}]")

    # Player movement for each input
    for indiv_input in input("> ").lower():
        if indiv_input not in (controls.movement_keybinds | controls.player_action_keybinds | controls.ui_keybinds):
            break
        clear()
        run_input(indiv_input)

        # If user has reached the win condition
        if menu.curr_stage.score >= menu.curr_stage.score_req:
            clear()
            print(display(menu.curr_stage, False))
            print(f"\N{mushroom} collected: {menu.curr_stage.score}")
            win_screen()
            exit()

    print(display(menu.curr_stage, False))
    print(f"\N{mushroom}: {menu.curr_stage.score}")
