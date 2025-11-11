import os
import sys
import time
from mapper import stage_tile
import tiles
from player import character

class stage():
    def __init__(self, path):
        self.path = f"DLC\maps\{path}"

        if path == "": # If user enters without input, open the default map
            self.path = "DLC\default.txt"
        try:
            try:
                self.file = open(f"maps/{self.path}", "r") # Elif, check the maps folder first if map is there
            except FileNotFoundError:
                self.file = open(f"{self.path}", "r") # Elif, check the main folder
        except FileNotFoundError:
            print(f"Error: Stage file {self.path} not found.") # Else, the txt file cannot be found
            exit()

    def start(self):
        self.read_lines = self.file.readlines()
        self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
        self.listed_file = list(x.rstrip() for x in self.read_lines[1:])
        if any((self.y != len(self.listed_file), self.x != len(self.listed_file[0]))): # Insurance for grid dimensions
            print(f"Error: Initialized forest dimension {self.y}, {self.x} does not match actual forest dimension {len(self.listed_file)}, {len(self.listed_file[0])}.")
            exit()

        self.score = 0
        self.score_req = 0
        self.inventory = None
        self.object_list = list([0,] * self.x for y in range(self.y))
        self.curr_locs = []
        self.characters = []
        self.floor_interactions = {}

        for y in range(self.y):
            for x in range(self.x):
                tile_being_loaded = self.listed_file[y][x]

                if tile_being_loaded == "+":
                    self.score_req += 1
            
                if tile_being_loaded == "L":
                    self.curr_locs.append(([x,y], None))

                self.object_list[y][x] = stage_tile(None, ".", (x,y), self)

                if tile_being_loaded in tiles.tile_object_tags:
                    self.object_list[y][x].tile_object = tile_being_loaded

                elif tile_being_loaded in tiles.tile_floor_tags:
                    self.object_list[y][x].tile_floor = tile_being_loaded

                    #initializes portals
                    if "portal" in tiles.tile_floor_tags[tile_being_loaded]:

                        #try to link the second portal to first portal, but if first portal doesnt exist in the dictionary, just make add it to the dictionary to be linked
                        try:
                            self.floor_interactions[tile_being_loaded][(x,y)] = self.floor_interactions[tile_being_loaded][()]
                            self.floor_interactions[tile_being_loaded][self.floor_interactions[tile_being_loaded][()]] = (x,y)
                            del self.floor_interactions[tile_being_loaded][()]
                            #print("paired")
                        except KeyError:
                            self.floor_interactions[tile_being_loaded] = {(x,y): (), () : (x,y)}
                            #print("keyerr")
        #print(self.floor_interactions)
        #time.sleep(50)

        for char_loc in self.curr_locs:
            self.characters.append(character(char_loc[0], (self.x, self.y), char_loc[1], self))



class Menu:
    def __init__(self, prev_screen):
        self.main = self.main_menu
        self.control = self.control_menu
        self.map_select = self.map_selection
        self.prev = prev_screen
    
    def main_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        ----------------------------------------
        |                                      |
        |      Put the fries in the bag        |
        |                                      |
        |                                      |
        |                Play                  |
        |              Controls                |
        |                Quit                  |
        ----------------------------------------
        """)
        self.player_input = input("> ").lower()
        if self.player_input in ("play", "p", "pl", "pla"):
            os.system("cls" if os.name == "nt" else "clear")
            self.map_selection()
        elif self.player_input in ("controls", "c", "co", "con", "cont", "contr", "contro", "control"):
            self.control_menu()
        elif self.player_input in ("quit", "q", "qu", "qui"):
            sys.exit()
        else:
            self.main_menu()

    def control_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("""
        ..................................
        .            Controls:           .
        .                                .
        .         W - Move up            .
        .         A - Move left          .
        .         S - Move down          .
        .         D - Move right         .
        .         P - Pick up item       .
        .         ! - Reset map          .
        .                                .
        ..................................
        """)
        input("Press Enter to go back...")
        if self.prev == "main":
            self.prev = "main"
            self.main_menu()


    def map_selection(self):
        print("""
        ..................................
        |                                |
        |      Please type your map      |
        |                                |
        |      Make sure file is in      |
        |          Maps folder           |
        |                                |
        |          Press Enter           |
        |        for default map         |
        |                                |
        ..................................
        """)
        os.system("dir /b /a-d DLC\maps\*.txt") # Prints all the files in the maps subfolder
        self.chosenmap = input("Please type your map: ")
        self.curr_stage = stage(self.chosenmap)
        self.curr_stage.start()
        #mapList = os.system("dir /b /a-d *.txt")
    

    

def win_screen():
    os.system("cls" if os.name == "nt" else "clear")
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
    sys.exit()

if __name__ == "__main__":
    menu = Menu("main")
    x = getattr(menu, "main")
    x()