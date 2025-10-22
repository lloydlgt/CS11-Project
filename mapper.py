import os
import tiles
class stage():
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "r")
        self.read_lines = self.file.readlines()
        self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
        print(self.x, self.y)
        self.listed_file = list(x.rstrip() for x in self.read_lines[1:])
        self.indiv_char = list(char for strings in self.listed_file for char in strings)
        self.maplist = self.convert()
        self.score = 0
        self.inventory = ""
        self.interactable_objects = []
        self.curr_locs = []
        for y in range(self.y):
            # change this to accomodate for multiple player characters
            for x in range(self.x):
                print(y,x)
                if self.maplist[y][x] == "\N{adult}":
                    self.curr_locs.append(([x,y], "  "))
                elif "interactable" in tiles.tile_tags[tiles.tiles_translate[self.maplist[y][x]]]:
                    self.interactable_objects.append(stage_object(self.maplist[y][x], (x,y), "  ", (self.x, self.y)))

    def convert(self):
        self.emoji = tiles.translate_tiles
        newlist = []
        for rows in self.listed_file:
            newlist.append(list(self.emoji.get(y) for y in rows))
        return newlist
    
    def grab_item(self, loc: tuple[int, int]):
        ans = input("grab item(yes or no)? ").lower()
        if ans == "yes":
            return self.maplist[loc[1]][loc[0]], False
        elif ans == "no":
            return True
        else:
            print("invalid input")
            self.grab_item()
        


class stage_object:

    def __init__(self, object: str, coords: tuple[int,int], curr_tile: str, bounds: tuple[int,int]):
        self.object = object
        self.x_coords, self.y_coords = coords[0], coords[1]
        self.curr_tile = curr_tile
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]

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
    

if __name__ == "__main__":
    mapstr = ""
    lvl1 = stage("level.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(lvl1.indiv_char)
