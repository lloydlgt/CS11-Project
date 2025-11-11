import os
import tiles
import time
from menu import death_screen

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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

    def move(self, movement: tuple[int,int]):
        if not (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            return None
        else:
            from mapper import display
        new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]
        
        next_tile = self.curr_stage.object_list[new_y][new_x]
        next_tile_floor_tags = tiles.tile_floor_tags[next_tile.tile_floor]
        if next_tile.tile_object:
            next_tile_object_tags = tiles.tile_object_tags[next_tile.tile_object]
        else:
            next_tile_object_tags = {}

        if "interactable" in next_tile_object_tags:
            if "pushable" in next_tile_object_tags:
                next_tile.move(movement)
                        
            if "choppable" in next_tile_object_tags:
                if self.curr_stage.inventory in {"x"}:
                    self.curr_stage.object_list[new_y][new_x].tile_object = None
                    self.curr_stage.inventory = None

            if "burnable" in next_tile_object_tags:
                if self.curr_stage.inventory in {"*"}:
                    self.burn = {(new_x, new_y)}
                    self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                    while self.burn:
                        # Creates fire and makes a copy for adjacent trees
                        self.temp_burn = self.burn.copy()
                        for trees in self.burn:
                            self.curr_stage.object_list[trees[1]][trees[0]].tile_object = None

                        # Checks adjacent cells for trees
                        self.burn.clear() 
                        for trees in self.temp_burn:
                            for direction in self.directions:
                                if 0 <= trees[0] + direction[0] < self.x_bound and 0 <= trees[1] + direction[1] < self.y_bound:
                                    if self.curr_stage.object_list[trees[1] + direction[1]][trees[0] + direction[0]].tile_object and "burnable" in tiles.tile_object_tags[self.curr_stage.object_list[trees[1] + direction[1]][trees[0] + direction[0]].tile_object]:
                                        self.burn.add((trees[0] + direction[0], trees[1] + direction[1]))
                    self.curr_stage.inventory = None            

        next_tile = self.curr_stage.object_list[new_y][new_x]
        next_tile_floor_tags = tiles.tile_floor_tags[next_tile.tile_floor]
        if next_tile.tile_object:
            next_tile_object_tags = tiles.tile_object_tags[next_tile.tile_object]
        else:
            next_tile_object_tags = {}

        if "can_move_to" in next_tile_floor_tags:
            if not next_tile_object_tags:
                next_tile.tile_object = "L"
                self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                self.curr_tile = None
                self.x_coords, self.y_coords = new_x, new_y
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
                        self.x_coords, self.y_coords = new_x, new_y

                else:
                    temp = next_tile.tile_object
                    next_tile.tile_object = "L"
                    self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                    self.curr_tile = temp
                    self.x_coords, self.y_coords = new_x, new_y

if __name__ == "__main__":
    print("Wrong file.")
