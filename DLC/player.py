import os
import tiles
from mapper import stage 
import time
from menu import death_screen

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
        #print("move checking")
        #time.sleep(2)
        if not movement:
            return
        if 0 <= movement[0] < self.curr_stage.x and 0 <= movement[1] < self.curr_stage.y:
            next_tile = self.curr_stage.object_list[movement[1]][movement[0]]
            next_tile_floor_tags = tiles.tile_floor_tags[tiles.tiles_translate[next_tile.tile_floor]]
            if next_tile.tile_object != None:
                next_tile_object_tags = tiles.tile_object_tags[tiles.tiles_translate[next_tile.tile_object]]
            else:
                next_tile_object_tags = {}
            if "interactable" in next_tile_object_tags:
                #print("interacting")
                #time.sleep(2)
                if "pushable" in next_tile_object_tags:
                    #print("pushing")
                    #time.sleep(2)
                    obj_direction = getattr(next_tile, "move_" + direction)
                    next_tile.move(obj_direction())
                            
                elif "choppable" in next_tile_object_tags or "burnable" in next_tile_object_tags:
                        if self.curr_stage.inventory in {"x"}:
                            self.curr_stage.object_list[movement[1]][movement[0]].tile_object = None
                            self.curr_stage.inventory = "Empty"

                        if self.curr_stage.inventory in {"*"}:
                            self.burn = {(movement[0], movement[1])}
                            self.animation = set()
                            self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                            while self.burn or self.animation:
                                os.system("cls" if os.name == "nt" else "clear") 
                                mapstr = ""
                                
                                # Creates fire and makes a copy for adjacent trees
                                self.temp_burn = self.burn.copy()
                                for self.trees in self.burn:
                                    self.curr_stage.object_list[self.trees[1]][self.trees[0]].tile_object = '\N{fire}'
                                

                                # Prints map
                                for objlist in self.curr_stage.object_list:
                                    for obj in objlist:
                                        if obj.tile_object:
                                            mapstr += obj.tile_object
                                        else:
                                            mapstr += obj.tile_floor
                                    mapstr += "\n"
                                print(mapstr)
                                print(f"\N{mushroom}: {self.curr_stage.score}")

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
                                            if self.curr_stage.object_list[self.trees[1] + self.direction[1]][self.trees[0] + self.direction[0]].tile_object != None and "burnable" in tiles.tile_object_tags[tiles.tiles_translate[self.curr_stage.object_list[self.trees[1] + self.direction[1]][self.trees[0] + self.direction[0]].tile_object]]:
                                               self.burn.add((self.trees[0] + self.direction[0], self.trees[1] + self.direction[1]))
                                time.sleep(0.5)
                            os.system("cls" if os.name == "nt" else "clear")
                            self.curr_stage.inventory = "EMPTY"            
            next_tile = self.curr_stage.object_list[movement[1]][movement[0]]
            next_tile_floor_tags = tiles.tile_floor_tags[tiles.tiles_translate[next_tile.tile_floor]]
            if next_tile.tile_object != None:
                next_tile_object_tags = tiles.tile_object_tags[tiles.tiles_translate[next_tile.tile_object]]
            else:
                next_tile_object_tags = {}

            if "can_move_to" in next_tile_floor_tags:
                if next_tile.tile_object == None:
                    #print("moving")
                    #time.sleep(2)
                    next_tile.tile_object = "\N{adult}"
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
                            next_tile.tile_object = "\N{adult}"
                            self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                            self.curr_tile = None
                            self.x_coords, self.y_coords = movement
                    else:
                        temp = next_tile.tile_object
                        next_tile.tile_object = "\N{adult}"
                        self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                        self.curr_tile = temp
                        self.x_coords, self.y_coords = movement
        #print("done")
        #time.sleep(2)
if __name__ == "__main__":
    for i in range(100):
        print("WRONG FILE LMAO           " * 3)
