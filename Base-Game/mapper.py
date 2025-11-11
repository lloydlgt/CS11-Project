import os
import tiles
import time
from player import character

class stage():
    def __init__(self, path):
        self.path = path

        try:
            # Setup the map variables and insure actual dimensions match initialized forest dimensions
            with open(f"{self.path}", "r") as file:
                self.file = file
                self.read_lines = self.file.readlines()
                self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
                self.listed_file = list(x.rstrip() for x in self.read_lines[1:])

                if any((self.y != len(self.listed_file), self.x != len(self.listed_file[0]))): # Insurance for grid dimensions
                    print(f"Error: Initialized forest dimension {self.y}, {self.x} does not match actual forest dimension {len(self.listed_file)}, {len(self.listed_file[0])}.")
                    exit()        
        except FileNotFoundError:
            # Handles inputting a non-existent stage file
            print(f"Error: Stage file {self.path} not found.")
            exit()

        # Game stats
        self.score = 0
        self.score_req = 0
        self.inventory = None
        self.object_list = list([0,] * self.x for y in range(self.y))
        self.curr_locs = []
        self.characters = []

        # "Load" up the main map
        for y in range(self.y):
            for x in range(self.x):
                if self.listed_file[y][x] == "+":
                    self.score_req += 1
                if self.listed_file[y][x] == "L":
                    self.curr_locs.append(([x,y], None))
                self.object_list[y][x] = stage_tile(None, ".", (x,y), self)
                if self.listed_file[y][x] in tiles.tile_object_tags:
                    self.object_list[y][x].tile_object = self.listed_file[y][x]
                elif self.listed_file[y][x] in tiles.tile_floor_tags:
                    self.object_list[y][x].tile_floor = self.listed_file[y][x]

        # Save the character ("Laro") positions
        for char_loc in self.curr_locs:
            self.characters.append(character(char_loc[0], (self.x, self.y), char_loc[1], self))
    

class stage_tile:
    __slots__ = ("tile_object", "tile_floor", "x_coords", "y_coords", "x_bound", "y_bound", "curr_stage")
    def __init__(self, tile_object: str, tile_floor: str, coords: tuple[int,int], curr_stage: stage):
        self.tile_object = tile_object
        self.tile_floor = tile_floor
        self.x_coords, self.y_coords = coords[0], coords[1]
        self.x_bound = curr_stage.x
        self.y_bound = curr_stage.y
        self.curr_stage = curr_stage
        
    def move(self, movement: tuple[int,int]):
        if (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]
            move_tile = self.curr_stage.object_list[new_y][new_x]
            
            if "reactive" in tiles.tile_floor_tags[move_tile.tile_floor]:
                move_tile.tile_floor = tiles.tile_reactions[(self.tile_object, move_tile.tile_floor)]
                self.tile_object = None
            elif move_tile.tile_object == None:
                move_tile.tile_object = self.tile_object
                self.tile_object = None
            elif "reactive" in tiles.tile_object_tags[move_tile.tile_object]:
                pass

def display(curr_stage: stage, ASCII:bool):
    mapstr = ""
    for objlist in curr_stage.object_list:
            for obj in objlist:
                if obj.tile_object:
                    if ASCII == True:
                        mapstr += obj.tile_object
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_object]
                else:
                    if ASCII == True:
                        mapstr += obj.tile_floor
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_floor]
            mapstr += "\n"
    return mapstr


if __name__ == "__main__":
    mapstr = ""
    lvl1 = stage("default.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(lvl1.listed_file)