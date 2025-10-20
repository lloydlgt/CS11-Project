import os # tite
import sys
import time
from menu import main_menu, control_menu
from mapper import map_converter
from player import player
#dfrom booter import launch
import controls
main_menu()
map_1 = map_converter("est.txt")

#make this a comprehension for multiple player characters
char = player(map_1.curr_loc, {}, (len(map_1.maplist[0]), len(map_1.maplist)))


while True:
    os.system("cls" if os.name == "nt" else "clear")
    #print map balls
    mapstr = ""
    for row in map_1.maplist:
        mapstr += "".join(row) + "\n"
    print(mapstr)

    #for loop this later for every character
    #move player
    for x in input("> "):
        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")

        # movement inputs
        if x.lower() in controls.movement_keybinds: #and map isnt cleared
            movement = getattr(char, "move_" + controls.movement_keybinds[x.lower()])
            rech = map_1.move(movement())
            char.rewind(rech)

        elif x.lower() in controls.ui_keybinds:
            ...
            
        mapstr = ""
        for row in map_1.maplist:
            mapstr += "".join(row) + "\n"
        print(mapstr)

