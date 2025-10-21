import os
import tiles
class map_converter():
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "r")
        self.listed_file = list(x.rstrip() for x in self.file.readlines())
        self.maplist = self.convert()
        for y in range(len(self.maplist)):
            # change this to accomodate for multiple player characters
            if "\N{adult}" in self.maplist[y]:
                self.curr_loc = self.maplist[y].index("\N{adult}"), y
                self.current_tile = "  "
    
    def convert(self):
        self.emoji = tiles.translate_tiles
        newlist = []
        for rows in self.listed_file:
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
    ...




        





