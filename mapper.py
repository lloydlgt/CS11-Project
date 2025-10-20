import os
import tiles
class map_converter():
    
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "r")
        self.listed_file = list(x.rstrip() for x in self.file.readlines())
        self.maplist = self.convert()
        for y in range(len(self.maplist)):
            if "\N{adult}" in self.maplist[y]:
                self.lloyd = self.maplist[y].index("\N{adult}"), y

    
    def convert(self):
        self.emoji = tiles.translate_tiles
        newlist = []
        for rows in self.listed_file:
            newlist.append(list(self.emoji.get(y) for y in rows))
        return newlist
    
    def change(self, loc: tuple[int, int]):
        if "can_move_to" in tiles.tile[tiles.tiles_translate[self.maplist[loc[1]][loc[0]]]]:
            self.maplist[loc[1]][loc[0]] = "\N{adult}"
            self.maplist[self.lloyd[1]][self.lloyd[0]] = "  "
            self.lloyd = loc

            
    
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




        





