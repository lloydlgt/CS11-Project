from menu import main_menu, control_menu
import tiles
from mapper import map_converter 

class player:
    def __init__(self, location: tuple[int, int], bounds: tuple[int,int], curr_tile: str, map_1: map_converter):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.bounds = self.x_bound, self.y_bound
        self.curr_tile = curr_tile
        self.map_1 = map_1
    
    def move_up(self):
        """ # move up
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
                    self.map_1.maplist[self.prev_coords[1]][self.prev_coords[0]] = self.curr_tile
                    self.curr_tile = self.map_1.maplist[loc[1]][loc[0]]
                    self.map_1.maplist[loc[1]][loc[0]] = "\N{adult}"
                    self.x_coords, self.y_coords = loc
                    # item logic goes here
                    return False
            
            return True
        else:
            return True
        

    def mover(self, direction: str, next_tile: str):
        if tiles.tile[next_tile]:
            ...
        if direction in {"menu", "m", "me", "men"}:
            main_menu()
        elif direction in {"controls", "c", "co", "con", "cont", "contr", "contro", "control"}:
            control_menu()
        else:
            return self.move()
        
        self.coords = self.x_coords, self.y_coords
