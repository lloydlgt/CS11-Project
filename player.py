import tiles
from mapper import stage 

class player:
    def __init__(self, location: tuple[int, int], bounds: tuple[int,int], curr_tile: str, curr_stage: stage, items: str, score: int):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.bounds = self.x_bound, self.y_bound
        self.curr_tile = curr_tile
        self.curr_stage = curr_stage
        self.items = items
    
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
        if 0 <= loc[0] < len(self.curr_stage.maplist[0]) and 0 <= loc[1] < len(self.curr_stage.maplist):
            tags = tiles.tile_tags[tiles.tiles_translate[self.curr_stage.maplist[loc[1]][loc[0]]]]
            if "pushable" in tags:
                #make dict of coords
                #check if rock moved loc is in rock loc dict
                #if that then move the rock then put in the saved tile in dict
                # also account for player curr tile :) 
                ...

            if "can_move_to" in tags: # If you can move to the next tile
                    self.curr_stage.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile #  Sets the tile you are currently on to what it was beforehand
                    self.curr_tile = self.curr_stage.maplist[loc[1]][loc[0]] # Saves the tile you're going to
                    self.curr_stage.maplist[loc[1]][loc[0]] = "\N{adult}" # Moves you to the next tile
                    self.x_coords, self.y_coords = loc # Updates the player's coordinates
                    """if "manual_pickup" in tags and self.items in {"Empty"}:
                        mapstr = ""
                        for row in self.curr_stage.maplist:
                            mapstr += "".join(row) + "\n"
                        print(mapstr)
                        if pick_up_prompt in {'P', 'p'}:
                            self.items = tiles.tiles_translate[self.curr_tile]
                            self.curr_tile = """
                    if "win_condition" in tags:
                        self.curr_tile = "  "
                        self.curr_stage.score += 1
                        

                    return False
            
            if "choppable" in tags or "burnable" in tags:
                    if self.items in {"x"}:
                        self.curr_stage.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile
                        self.curr_tile = "  "
                        self.curr_stage.maplist[loc[1]][loc[0]] = "\N{adult}"
                        self.x_coords, self.y_coords = loc
                        self.items = "Empty"
                        return False
                    if self.items in {"*"}:
                        self.curr_stage.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile
                        self.curr_tile = "  "

                        self.burn = {(loc[1], loc[0])}
                        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                        while self.burn:
                            self.temp_burn = self.burn.copy()
                            for self.trees in self.burn:
                                self.curr_stage.maplist[self.trees[0]][self.trees[1]] = "  "
                            self.burn.clear()
                            for self.trees in self.temp_burn:
                                for self.direction in self.directions: # Bakit baliktad yung x, y dito wtf?!?
                                    if 0 <= self.trees[1] + self.direction[1] < self.x_bound and 0 <= self.trees[0] + self.direction[0] < self.y_bound:
                                        if self.curr_stage.maplist[self.trees[0] + self.direction[0]][self.trees[1] + self.direction[1]] == tiles.translate_tiles['T']:
                                            self.burn.add((self.trees[0] + self.direction[0], self.trees[1] + self.direction[1]))

                        self.curr_stage.maplist[loc[1]][loc[0]] = "\N{adult}"
                        self.x_coords, self.y_coords = loc
                        self.items = "Empty"
                        return False  

            return True
        else:
            return True

