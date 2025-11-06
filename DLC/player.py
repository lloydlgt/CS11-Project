import os
import tiles
import time
from menu import death_screen

class character:
    def __init__(self, location: tuple[int, int], bounds: tuple[int,int], curr_tile: str, curr_stage):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.bounds = self.x_bound, self.y_bound
        self.curr_tile = curr_tile
        self.curr_stage = curr_stage
    
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

    def move(self, movement: tuple[int,int], direction: str):
       
        if not movement:
            return
        
        if 0 <= movement[0] < self.curr_stage.x and 0 <= movement[1] < self.curr_stage.y:

            next_tile = self.curr_stage.object_list[movement[1]][movement[0]]
            next_tile_floor_tags = tiles.tile_floor_tags[next_tile.tile_floor]
            if next_tile.tile_object != None:
                next_tile_object_tags = tiles.tile_object_tags[next_tile.tile_object]
            else:
                next_tile_object_tags = {}

            if "interactable" in next_tile_object_tags:

                if "pushable" in next_tile_object_tags:
                    obj_direction = getattr(next_tile, "move_" + direction)
                    next_tile.move(obj_direction())
                            
                if "choppable" in next_tile_object_tags:
                    if self.curr_stage.inventory in {"x"}:
                        self.curr_stage.object_list[movement[1]][movement[0]].tile_object = None
                        self.curr_stage.inventory = None

                if "burnable" in next_tile_object_tags:
                    if self.curr_stage.inventory in {"*"}:
                        self.burn = {(movement[0], movement[1])}
                        self.animation = set()
                        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                        while self.burn or self.animation:
                            os.system("cls" if os.name == "nt" else "clear") 
                            
                            # Creates fire and makes a copy for adjacent trees
                            self.temp_burn = self.burn.copy()
                            for self.trees in self.burn:
                                self.curr_stage.object_list[self.trees[1]][self.trees[0]].tile_object = "@"
                            
                            
                            # Prints map
                            from mapper import display
                            print(display(self.curr_stage, False))

                            # Takes care of animation
                            for self.trees in self.animation:
                                self.curr_stage.object_list[self.trees[1]][self.trees[0]].tile_object = None
                            self.animation.clear()

                            # Checks adjacent cells for trees
                            self.burn.clear() 
                            for self.trees in self.temp_burn:
                                self.animation.add((self.trees[0], self.trees[1]))
                                for self.direction in self.directions:
                                    if 0 <= self.trees[0] + self.direction[0] < self.x_bound and 0 <= self.trees[1] + self.direction[1] < self.y_bound:
                                        if self.curr_stage.object_list[self.trees[1] + self.direction[1]][self.trees[0] + self.direction[0]].tile_object != None and "burnable" in tiles.tile_object_tags[self.curr_stage.object_list[self.trees[1] + self.direction[1]][self.trees[0] + self.direction[0]].tile_object]:
                                            self.burn.add((self.trees[0] + self.direction[0], self.trees[1] + self.direction[1]))
                            time.sleep(0.5)
                        os.system("cls" if os.name == "nt" else "clear")
                        self.curr_stage.inventory = None            

            next_tile = self.curr_stage.object_list[movement[1]][movement[0]]
            next_tile_floor_tags = tiles.tile_floor_tags[next_tile.tile_floor]
            if next_tile.tile_object != None:
                next_tile_object_tags = tiles.tile_object_tags[next_tile.tile_object]
            else:
                next_tile_object_tags = {}

            if "can_move_to" in next_tile_floor_tags:

                if next_tile.tile_object == None:
                    next_tile.tile_object = "L"
                    self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                    self.curr_tile = None
                    self.x_coords, self.y_coords = movement
                    if "death_on_touch" in next_tile_floor_tags:
                        death_screen()

                elif "item" in next_tile_object_tags:
                    if "auto_pickup" in next_tile_object_tags:
                        if "win_condition" in next_tile_object_tags:
                            next_tile.tile_object = None
                            self.curr_stage.score += 1
                            next_tile.tile_object = "L"
                            self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                            self.curr_tile = None
                            self.x_coords, self.y_coords = movement

                    else:
                        temp = next_tile.tile_object
                        next_tile.tile_object = "L"
                        self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                        self.curr_tile = temp
                        self.x_coords, self.y_coords = movement
        #print("done")
        #time.sleep(2)
if __name__ == "__main__":
    for i in range(100):
        print("WRONG FILE LMAO           " * 3)
