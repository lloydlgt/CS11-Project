import os
import tiles
class map_converter():
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "r")
        self.read_lines = self.file.readlines()
        self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
        print(self.x+ self.y)
        self.listed_file = list(x.rstrip() for x in self.read_lines[1:])
        self.maplist = self.convert()
        for y in range(len(self.maplist)):
            # change this to accomodate for multiple player characters
            if "\N{adult}" in self.maplist[y]:
                self.curr_loc = self.maplist[y].index("\N{adult}"), y
                self.current_tile = "  "
    
    def convert(self):
        self.emoji = tiles.translate_tiles
        newlist = []
        for rows in self.listed_file[1:]:
            newlist.append(list(self.emoji.get(y) for y in rows))
        return newlist

    def change(self, loc: tuple[int, int]):
        if not loc:
            return False
        if 0 <= loc[0] < len(self.maplist[0]) and 0 <= loc[1] < len(self.maplist):
            if "can_move_to" in tiles.tile_tags[tiles.tiles_translate[self.maplist[loc[1]][loc[0]]]]:
                    self.maplist[self.curr_loc[1]][self.curr_loc[0]] = self.current_tile
                    self.current_tile = self.maplist[loc[1]][loc[0]]
                    self.maplist[loc[1]][loc[0]] = "\N{adult}"
                    self.curr_loc = loc
                    # item logic goes here
                    return False
            elif "pushable" in tiles.tile_tags[tiles.tiles_translate[self.maplist[loc[1]][loc[0]]]]:
                #make dict of coords
                #check if rock moved loc is in rock loc dict
                #if that then move the rock then put in the saved tile in dict
                # also account for player curr tile :) 
                ...
            else:
                return True
        else:
            return True
    
    def grab_item(self, loc: tuple[int, int]):
        ans = input("grab item(yes or no)? ").lower()
        if ans == "yes":
            return self.maplist[loc[1]][loc[0]], False
        elif ans == "no":
            return True
        else:
            print("invalid input")
            self.grab_item()
        

if __name__ == "__main__":
    mapstr = ""
    lvl1 = map_converter("est.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(mapstr)




        





