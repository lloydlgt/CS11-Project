import os
import tiles
import time


class stage():
    def __init__(self, path):
        self.path = path

        if self.path == "": # If user enters without input, open the default map
            self.path = "default.txt"
        try:
            try:
                self.file = open(f"maps/{self.path}", "r") # Elif, check the maps folder first if map is there
            except FileNotFoundError:
                self.file = open(f"{self.path}", "r") # Elif, check the main folder
        except FileNotFoundError:
            print(f"Error: Stage file {self.path} not found.") # Else, the txt file cannot be found
            exit()

        self.read_lines = self.file.readlines()
        self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
        self.listed_file = list(x.rstrip() for x in self.read_lines[1:])
        if any((self.y != len(self.listed_file), self.x != len(self.listed_file[0]))): # Insurance for grid dimensions
            print(f"Error: Initialized forest dimension {self.y}, {self.x} does not match actual forest dimension {len(self.listed_file)}, {len(self.listed_file[0])}.")
            exit()

        self.score = 0
        self.score_req = 0
        self.inventory = ""
        self.object_list = list([0,] * self.x for y in range(self.y))
        self.curr_locs = []

        for y in range(self.y):
            for x in range(self.x):
                print(x,y)
                if self.listed_file[y][x] == "+":
                    self.score_req += 1
                if self.listed_file[y][x] == "L":
                    #print(([x,y], "  ", "player found"))
                    #time.sleep(2)
                    self.curr_locs.append(([x,y], None))
                self.object_list[y][x] = stage_tile(None, "  ", (x,y), self)
                if self.listed_file[y][x] in tiles.tile_object_tags:
                    self.object_list[y][x].tile_object = self.convert(self.listed_file[y][x])
                elif self.listed_file[y][x] in tiles.tile_floor_tags:
                    self.object_list[y][x].tile_floor = self.convert(self.listed_file[y][x])

    def convert(self, obj: str):
        return tiles.translate_tiles[obj]
    

class stage_tile:
    __slots__ = ("tile_object", "tile_floor", "x_coords", "y_coords", "x_bound", "y_bound", "curr_stage")
    def __init__(self, tile_object: str, tile_floor: str, coords: tuple[int,int], curr_stage: stage):
        self.tile_object = tile_object
        self.tile_floor = tile_floor
        self.x_coords, self.y_coords = coords[0], coords[1]
        self.x_bound = curr_stage.x
        self.y_bound = curr_stage.y
        self.curr_stage = curr_stage

    # if the object can move this will move it
    def move_up(self):
        if self.y_coords - 1 >= 0:
            return self.x_coords, self.y_coords - 1

    def move_down(self):
        if self.y_coords + 1 < self.y_bound:
            return self.x_coords, self.y_coords + 1
        
    def move_left(self):
        if self.x_coords - 1 >= 0:
            return self.x_coords - 1, self.y_coords
        
    def move_right(self):
        if self.x_coords + 1 < self.x_bound:
            return self.x_coords + 1, self.y_coords
        
    def move(self, movement: tuple[int,int]):
        if movement:
        #if "can_move_to" in tiles.tile_object_tags[tiles.tiles_translate[self.curr_stage[movement[1]][movement[0]].tile_object]]:
            if "reactive" in tiles.tile_floor_tags[tiles.tiles_translate[self.curr_stage.object_list[movement[1]][movement[0]].tile_floor]]:
                self.curr_stage.object_list[movement[1]][movement[0]].tile_floor = tiles.translate_tiles[tiles.tile_reactions[(tiles.tiles_translate[self.tile_object], tiles.tiles_translate[self.curr_stage.object_list[movement[1]][movement[0]].tile_floor])]]
                self.tile_object = None
            elif self.curr_stage.object_list[movement[1]][movement[0]].tile_object == None:
                self.curr_stage.object_list[movement[1]][movement[0]].tile_object = self.tile_object
                self.tile_object = None
            elif "reactive" in tiles.tile_object_tags[tiles.tiles_translate[self.curr_stage.object_list[movement[1]][movement[0]].tile_object]]:
                ...
            

if __name__ == "__main__":
    mapstr = ""
    lvl1 = stage("level.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(lvl1.listed_file)
