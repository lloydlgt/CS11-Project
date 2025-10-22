import tiles
from mapper import stage 
import time
class player:
    def __init__(self, location: tuple[int, int], bounds: tuple[int,int], curr_tile: str, curr_stage: stage):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.bounds = self.x_bound, self.y_bound
        self.curr_tile = curr_tile
        self.curr_stage = curr_stage
    
    def move_up(self):
        """ #move up
        move up
        """
        if self.y_coords - 1 >= 0:
            self.prev_coords = self.x_coords, self.y_coords
            self.y_coords -= 1
            self.direction = "up"
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

    def move(self, loc: tuple[int,int], direction: str):
        if not loc:
            return False
        if 0 <= loc[0] < len(self.curr_stage.maplist[0]) and 0 <= loc[1] < len(self.curr_stage.maplist):
            tags = tiles.tile_tags[tiles.tiles_translate[self.curr_stage.maplist[loc[1]][loc[0]]]]
            if "interactable" in tags:
                if "pushable" in tags:
                    for obj in self.curr_stage.interactable_objects:
                        if (loc[0], loc[1]) == (obj.x_coords, obj.y_coords):
                            push_obj = obj
                            break
                    obj_direction = getattr(push_obj, "move_" + direction)
                    push_loc = obj_direction()
                    if 0 <= push_loc[0] < self.x_bound and 0 <= push_loc[1] < self.y_bound:
                        if "can_move_to" in tiles.tile_tags[tiles.tiles_translate[self.curr_stage.maplist[push_loc[1]][push_loc[0]]]]:
                            self.curr_stage.maplist[self.y_coords][self.x_coords] = push_obj.curr_tile
                            push_obj.curr_tile = self.curr_stage.maplist[push_loc[1]][push_loc[0]]
                            self.curr_stage.maplist[push_loc[1]][push_loc[0]] = push_obj.object
                            push_obj.x_coords, push_obj.y_coords = push_loc[0], push_loc[1]
                    

                elif "choppable" in tags or "burnable" in tags:
                        if self.curr_stage.inventory in {"x"}:
                            self.curr_stage.maplist[loc[1]][loc[0]] = "  "
                            self.curr_stage.inventory = "Empty"
                        if self.curr_stage.inventory in {"*"}:


                            self.burn = {(loc[0], loc[1])}
                            self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                            while self.burn:
                                self.temp_burn = self.burn.copy()
                                for self.trees in self.burn:
                                    self.curr_stage.maplist[self.trees[1]][self.trees[0]] = "  "
                                self.burn.clear()
                                for self.trees in self.temp_burn:
                                    for self.direction in self.directions:
                                        if 0 <= self.trees[0] + self.direction[0] < self.x_bound and 0 <= self.trees[1] + self.direction[1] < self.y_bound:
                                            if self.curr_stage.maplist[self.trees[1] + self.direction[1]][self.trees[0] + self.direction[0]] == tiles.translate_tiles['T']:
                                                self.burn.add((self.trees[0] + self.direction[0], self.trees[1] + self.direction[1]))
                            self.curr_stage.inventory = "EMPTY" 
                    
            if "can_move_to" in tags: # If you can move to the next tile
                #print("moving")
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
                #time.sleep(1)
                return False
            return True
        else:
            return True

if __name__ == "__main__":
    for i in range(100):
        print("WRONG FILE LMAO           " * 3)
