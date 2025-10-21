import tiles
from mapper import map_converter 

class player:
    def __init__(self, location: tuple[int, int], bounds: tuple[int,int], curr_tile: str, map_1: map_converter, items: str, score: int):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.bounds = self.x_bound, self.y_bound
        self.curr_tile = curr_tile
        self.map_1 = map_1
        self.items = items
        self.score = score
    
    def move_up(self):
        """ #move up
        move up
        """
        if self.y_coords - 1 >= 0:
            self.prev_coords = self.x_coords, self.y_coords
            self.y_coords -= 1
            return self.x_coords, self.y_coords

    def move_down(self):
        if self.y_coords + 1 < self.y_bound:
            self.prev_coords = self.x_coords, self.y_coords
            self.y_coords += 1
            return self.x_coords, self.y_coords
        
    def move_left(self):
        if self.x_coords - 1 >= 0:
            self.prev_coords = self.x_coords, self.y_coords
            self.x_coords -= 1
            return self.x_coords, self.y_coords
        
    def move_right(self):
        if self.x_coords + 1 < self.x_bound:
            self.prev_coords = self.x_coords, self.y_coords
            self.x_coords += 1
            return self.x_coords, self.y_coords
        
    def rewind(self, state: bool):
        if state == True:
            self.x_coords = self.prev_coords[0]
            self.y_coords = self.prev_coords[1]

    def move(self, loc: tuple[int,int]):
        if not loc:
            return False
        if 0 <= loc[0] < len(self.map_1.maplist[0]) and 0 <= loc[1] < len(self.map_1.maplist):
            tags = tiles.tile_tags[tiles.tiles_translate[self.map_1.maplist[loc[1]][loc[0]]]]
            if "pushable" in tags:
                #make dict of coords
                #check if rock moved loc is in rock loc dict
                #if that then move the rock then put in the saved tile in dict
                # also account for player curr tile :) 
                ...

            if "can_move_to" in tags:
                    self.map_1.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile # If you move away from current tile, this is the tile you are in before moving 
                    self.curr_tile = self.map_1.maplist[loc[1]][loc[0]] # The tile you're currently on
                    self.map_1.maplist[loc[1]][loc[0]] = "\N{adult}" # Sets the tile you moved to into the player (Adult)
                    self.x_coords, self.y_coords = loc # The location of the current adult
                    if "manual_pickup" in tags and self.items in {"Empty"}:
                        mapstr = ""
                        for row in self.map_1.maplist:
                            mapstr += "".join(row) + "\n"
                        print(mapstr)
                        pick_up_prompt = input("Press [P] to pick up item: ")
                        if pick_up_prompt in {'P', 'p'}:
                            self.items = tiles.tiles_translate[self.curr_tile]
                            self.curr_tile = "  "
                    if "win_condition" in tags:
                        self.curr_tile = "  "
                        self.score += 1
                        

                    return False
            
            if "choppable" or "burnable" in tags:
                    if self.items in {"x"}:
                        self.map_1.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile
                        self.curr_tile = "  "
                        self.map_1.maplist[loc[1]][loc[0]] = "\N{adult}"
                        self.x_coords, self.y_coords = loc
                        self.items = "Empty"
                        return False
                    if self.items in {"*"}:
                        self.map_1.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile
                        self.curr_tile = "  "

                        self.burn = {(loc[1], loc[0])}
                        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                        while self.burn:
                            self.temp_burn = self.burn.copy()
                            for self.trees in self.burn:
                                self.map_1.maplist[self.trees[0]][self.trees[1]] = "  "
                            self.burn.clear()
                            for self.trees in self.temp_burn:
                                for self.direction in self.directions: # Bakit baliktad yung x, y dito wtf?!?
                                    if 0 <= self.trees[1] + self.direction[1] < self.x_bound and 0 <= self.trees[0] + self.direction[0] < self.y_bound:
                                        if self.map_1.maplist[self.trees[0] + self.direction[0]][self.trees[1] + self.direction[1]] == tiles.translate_tiles['T']:
                                            self.burn.add((self.trees[0] + self.direction[0], self.trees[1] + self.direction[1]))

                        self.map_1.maplist[loc[1]][loc[0]] = "\N{adult}"
                        self.x_coords, self.y_coords = loc
                        self.items = "Empty"
                        return False  

            return True
        else:
            return True

