import os
import tiles

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
        self.dead = False

    #updates next_tile variable to the real next tile
    def update_next_tile(self, x: int, y: int):
        self.next_tile = self.curr_stage.object_list[y][x]
        self.next_tile_floor_tags = tiles.tile_floor_tags[self.next_tile.tile_floor]
        if self.next_tile.tile_object is not None:
            self.next_tile_object_tags = tiles.tile_object_tags[self.next_tile.tile_object]
        else:
            self.next_tile_object_tags = {}

    #moves player without directly influencing the tile youre moving to (e.g. no pushing)
    def shift(self, movement: tuple[int,int]):
        if not (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            return False
        new_x, new_y = self.x_coords + movement[0], self.y_coords + movement[1]
        self.update_next_tile(new_x, new_y)

        if not ("can_move_to" in self.next_tile_object_tags or "can_move_to" in self.next_tile_floor_tags):
            return False
        #if object in next tile
        if "can_move_to" in self.next_tile_object_tags:

            #pickup
            if "auto_pickup" in self.next_tile_object_tags:
                temp = None
                if "win_condition" in self.next_tile_object_tags:
                    self.curr_stage.score += 1
            else:
                temp = self.next_tile.tile_object

            #moves the player
            self.next_tile.tile_object = "L"
            self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
            self.curr_tile = temp
            self.x_coords, self.y_coords = new_x, new_y
            return True
            
        elif "can_move_to" in self.next_tile_floor_tags and "can_move_to" not in self.next_tile_object_tags:
            from mapper import animate
            
            #no object, just move
            if not self.next_tile_object_tags:
                self.next_tile.tile_object = "L"
                self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                self.curr_tile = None
                prev_x, prev_y = self.x_coords, self.y_coords
                self.x_coords, self.y_coords = new_x, new_y
            #kill
                if "death_on_touch" in self.next_tile_floor_tags:
                    self.dead = True
                    

                if "button" in tiles.tile_floor_tags[self.curr_stage.object_list[prev_y][prev_x].tile_floor]:
                    self.curr_stage.update_gates(self.curr_stage.object_list[prev_y][prev_x].tile_floor)

                if "button" in self.next_tile_floor_tags:
                    self.curr_stage.update_gates(self.next_tile.tile_floor)

                if "lever" in self.next_tile_floor_tags:
                    self.curr_stage.update_gates(self.next_tile.tile_floor)
 
                #one way
                if "brittle" in self.next_tile_floor_tags:
                    if self.next_tile.tile_floor == "!":
                        self.curr_tile = "%"
                        self.curr_stage.object_list[self.y_coords][self.x_coords].tile_floor = "."
                    elif self.next_tile.tile_floor == "i":
                        self.curr_stage.object_list[self.y_coords][self.x_coords].tile_floor = "~"

                #ice
                if "slippery" in self.next_tile_floor_tags:
                    animate(self.curr_stage, 0.0625)    
                    return self.shift(movement)
                
                return True
        
        return False

    def move(self, movement: tuple[int,int]):
        if not (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            return
        else:
            from mapper import animate
        new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]

        self.update_next_tile(new_x,new_y)
        
        if "interactable" in self.next_tile_object_tags:

            #push
            if "pushable" in self.next_tile_object_tags:
                self.next_tile.move(movement)

            #chop
            if "choppable" in self.next_tile_object_tags:
                if self.curr_stage.inventory in {"x"}:
                    self.curr_stage.object_list[new_y][new_x].tile_object = None
                    self.curr_stage.inventory = None
            if "breakable" in self.next_tile_object_tags:
                if self.curr_stage.inventory in {"&"}:
                    self.curr_stage.object_list[new_y][new_x].tile_object = None
                    self.curr_stage.inventory = None
            #burn
            if "burnable" in self.next_tile_object_tags:
                if self.curr_stage.inventory in {"*"}:
                    self.burn = {(new_x, new_y)}
                    self.animation = set()
                    self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                    while self.burn or self.animation:
                        
                        # Creates fire and makes a copy for adjacent trees
                        self.temp_burn = self.burn.copy()
                        for trees in self.burn:
                            self.curr_stage.object_list[trees[1]][trees[0]].tile_object = "@"
                        
                        # Takes care of animation
                        for trees in self.animation:
                            self.curr_stage.object_list[trees[1]][trees[0]].tile_object = None
                        self.animation.clear()

                        # Checks adjacent cells for trees
                        self.burn.clear() 
                        for trees in self.temp_burn:
                            self.animation.add((trees[0], trees[1]))
                            for direction in self.directions:
                                if 0 <= trees[0] + direction[0] < self.x_bound and 0 <= trees[1] + direction[1] < self.y_bound:
                                    if self.curr_stage.object_list[trees[1] + direction[1]][trees[0] + direction[0]].tile_object and "burnable" in tiles.tile_object_tags[self.curr_stage.object_list[trees[1] + direction[1]][trees[0] + direction[0]].tile_object]:
                                        self.burn.add((trees[0] + direction[0], trees[1] + direction[1]))
                        animate(self.curr_stage, 0.125)  
                        
                    os.system("cls" if os.name == "nt" else "clear")
                    self.curr_stage.inventory = None            

        self.update_next_tile(new_x,new_y)

        if "can_move_to" in self.next_tile_floor_tags:
            moved = self.shift(movement)
            
            if not moved:
                return
            #conveyor
            if "conveyor" in self.next_tile_floor_tags:
                animate(self.curr_stage, 0.125)

                #where conveyor goes
                conveyor_dir = tiles.tile_special[self.next_tile.tile_floor]
                
                #try to shift() player
                self.shift(conveyor_dir)

            if "portal" in self.next_tile_floor_tags:
                animate(self.curr_stage, 0.125)
                #destination portal coords from the dictionary in initialization part in mapper
                destination_portal = self.curr_stage.interactions[self.next_tile.tile_floor][(self.x_coords,self.y_coords)]
                self.update_next_tile(*destination_portal,)

                #if destination has object, swap you and object, else just tp there
                if self.next_tile.tile_object:
                    self.curr_tile = self.next_tile.tile_object
                    self.next_tile.tile_object = None
                self.shift((destination_portal[0] - self.x_coords, destination_portal[1] - self.y_coords))


        #print("done")
        #time.sleep(2)

if __name__ == "__main__":
    for i in range(100):
        print("WRONG FILE LMAO           " * 3)
