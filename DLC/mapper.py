import os
import tiles
import time
from player import character

def animate(curr_stage, animation_time):
    os.system("cls" if os.name == "nt" else "clear") 
    print(display(curr_stage, False))
    time.sleep(animation_time)

class stage():
    def __init__(self, path):
        self.path = f"maps/{path}"

        if path == "": # If user enters without input, open the default map
            print("no map")
            self.path = "maps/default.txt"
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
        self.interactions = {}
        self.gates = {}

        for y in range(self.y):
            for x in range(self.x):
                tile_being_loaded = self.listed_file[y][x]

                if tile_being_loaded == "+":
                    self.score_req += 1
            
                if tile_being_loaded == "L":
                    self.curr_locs.append(([x,y], None))

                self.object_list[y][x] = stage_tile(None, ".", (x,y), self, False)

                if tile_being_loaded in tiles.tile_object_tags:
                    self.object_list[y][x].tile_object = tile_being_loaded

                    tile_initialized_object_tags = tiles.tile_object_tags[tile_being_loaded]

                    if "gate" in tile_initialized_object_tags:
                        try:
                            self.gates[tiles.tile_special[tile_being_loaded][0]].add((x,y))
                        except KeyError:
                            self.gates[tiles.tile_special[tile_being_loaded][0]] = {(x,y),}
                        self.object_list[y][x].tile_floor = tiles.tile_special[tile_being_loaded][1]
                        self.object_list[y][x].state = True
                    
                elif tile_being_loaded in tiles.tile_floor_tags:
                    self.object_list[y][x].tile_floor = tile_being_loaded

                    tile_initialized_floor_tags = tiles.tile_floor_tags[tile_being_loaded]
                    #initializes portals
                    if "portal" in tile_initialized_floor_tags:

                        #try to link the second portal to first portal, but if first portal doesnt exist in the dictionary, just make add it to the dictionary to be linked
                        try:
                            self.interactions[tile_being_loaded][(x,y)] = self.interactions[tile_being_loaded][()]
                            self.interactions[tile_being_loaded][self.interactions[tile_being_loaded][()]] = (x,y)
                            del self.interactions[tile_being_loaded][()]
                            #print("paired")
                        except KeyError:
                            self.interactions[tile_being_loaded] = {(x,y): (), () : (x,y)}
                            #print("keyerr")

                    if "door_floor" in tile_initialized_floor_tags:
                        try:
                            self.gates[tiles.tile_special[tile_being_loaded]].add((x,y))
                        except KeyError:
                            self.gates[tiles.tile_special[tile_being_loaded]] = {(x,y),}

        #print(self.interactions)
        #time.sleep(50)

        for char_loc in self.curr_locs:
            self.characters.append(character(char_loc[0], (self.x, self.y), char_loc[1], self))

    def update(self):
        for gate in self.gates:
            for gate_x, gate_y in self.gates[gate]:
                curr_gate = self.object_list[gate_y][gate_x]
                #if gate is supposed to be up, attempt to bring the wall up
                if curr_gate.state:
                    if not curr_gate.tile_object:
                        curr_gate.tile_object = tiles.tile_special[gate]
                    ...
                #bring the wall down
                elif not curr_gate.state:
                    if curr_gate.tile_object == tiles.tile_special[gate]:
                        curr_gate.tile_object = None

    def update_gates(self, key: str):
        for gate_x, gate_y in self.gates[key.lower()]:
            curr_gate = self.object_list[gate_y][gate_x]

            #reverses state
            curr_gate.state = not curr_gate.state
            
            

class stage_tile:
    __slots__ = ("tile_object", "tile_floor", "x_coords", "y_coords", "x_bound", "y_bound", "curr_stage", "state")
    def __init__(self, tile_object: str, tile_floor: str, coords: tuple[int,int], curr_stage: stage, state: bool):
        self.tile_object = tile_object
        self.tile_floor = tile_floor
        self.x_coords, self.y_coords = coords[0], coords[1]
        self.x_bound = curr_stage.x
        self.y_bound = curr_stage.y
        self.curr_stage = curr_stage
        self.state = False

    def shift(self, movement: tuple[int, int]):
        if not (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            return False
        new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]
        move_tile = self.curr_stage.object_list[new_y][new_x]

        if move_tile.tile_object and "can_move_to" in tiles.tile_floor_tags[move_tile.tile_floor]:
            return False
        
        move_tile.tile_object = self.tile_object
        self.tile_object = None

        if "button" in tiles.tile_floor_tags[self.tile_floor]:
            self.curr_stage.update_gates(self.tile_floor)

        if "button" in tiles.tile_floor_tags[move_tile.tile_floor]:
            self.curr_stage.update_gates(move_tile.tile_floor)

        if "lever" in tiles.tile_floor_tags[move_tile.tile_floor]:
            self.curr_stage.update_gates(move_tile.tile_floor)
 
        #ice
        if "slippery" in tiles.tile_floor_tags[move_tile.tile_floor]:
            animate(self.curr_stage, 0.0625)
            return move_tile.shift(movement)

        #portal
        if "portal" in tiles.tile_floor_tags[move_tile.tile_floor]:
            animate(self.curr_stage, 0.125)

            #sets portal destination
            destination_portal = self.curr_stage.interactions[move_tile.tile_floor][(new_x, new_y)]
            portal_destination = self.curr_stage.object_list[destination_portal[1]][destination_portal[0]]

            #switch places
            temp = move_tile.tile_object
            move_tile.tile_object = portal_destination.tile_object
            portal_destination.tile_object = temp
            
            return False

        return new_x, new_y


    def move(self, movement: tuple[int,int]):
        
        #attempt to move player and say if moved
        moved = self.shift(movement)

        #if didnt move then break
        if not moved:
            return
        
        #update destination
        new_curr_tile = self.curr_stage.object_list[moved[1]][moved[0]]
        
        
        #reaction e.g. paved tile
        if "reactive" in tiles.tile_floor_tags[new_curr_tile.tile_floor]:
            new_curr_tile.tile_floor = tiles.tile_reactions[(new_curr_tile.tile_object, new_curr_tile.tile_floor)]
            new_curr_tile.tile_object = None


        #conveyor
        elif "conveyor" in tiles.tile_floor_tags[new_curr_tile.tile_floor]:
            animate(self.curr_stage,0.125)
            conveyor_direction = tiles.tile_special[new_curr_tile.tile_floor]
            new_curr_tile.shift(conveyor_direction)
            
        elif new_curr_tile.tile_object and "reactive" in tiles.tile_object_tags[new_curr_tile.tile_object]:
            ...

        
        

def display(curr_stage: stage, ASCII:bool):
    mapstr = ""
    for objlist in curr_stage.object_list:
            for obj in objlist:
                if obj.tile_object:
                    if ASCII:
                        mapstr += obj.tile_object
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_object]
                else:
                    if ASCII:
                        mapstr += obj.tile_floor
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_floor]
            mapstr += "\n"
    return mapstr


if __name__ == "__main__":
    mapstr = ""
    lvl1 = stage("level.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(lvl1.listed_file)