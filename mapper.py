import os
import tiles
class map_converter():
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "r")
        self.read_lines = self.file.readlines()
        self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
        print(self.x, self.y)
        self.listed_file = list(x.rstrip() for x in self.read_lines[1:])
        self.maplist = self.convert()

        self.curr_locs = []
        for y in range(self.y):
            # change this to accomodate for multiple player characters
            for x in range(self.x):
                print(y,x)
                if self.maplist[y][x] == "\N{adult}":
                    self.curr_locs.append(([x,y], "  "))
    
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
        

if __name__ == "__main__":
    mapstr = ""
    lvl1 = map_converter("est.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(mapstr)




        





