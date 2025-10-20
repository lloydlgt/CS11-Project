import os # tite
import sys
import time
from menu import main_menu, control_menu
from mapper import map_converter
from player import player

main_menu()
map_1 = map_converter("D:\Programs\game_project\shit.txt")
char = player(map_1.lloyd, {})
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("gonna fuck lloyd tonight")
    #print map balls
    mapstr = ""
    for row in map_1.maplist:
        mapstr += "".join(row) + "\n"
    print(mapstr)
    print("hiiiiiiiii")
    #move player
    for x in input("> "):
        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")
        char.move(x)
        map_1.change(char.coords)
        mapstr = ""
        for row in map_1.maplist:
            mapstr += "".join(row) + "\n"
        print(mapstr)

