import os
import tiles
import time

def animate(curr_stage, animation_time):
    os.system("cls" if os.name == "nt" else "clear") 
    print(display(curr_stage, False))
    time.sleep(animation_time)
    

class stage_tile:
    __slots__ = ("tile_object", "tile_floor", "x_coords", "y_coords", "x_bound", "y_bound", "curr_stage")
    def __init__(self, tile_object: str, tile_floor: str, coords: tuple[int,int], curr_stage: stage):
        self.tile_object = tile_object
        self.tile_floor = tile_floor
        self.x_coords, self.y_coords = coords[0], coords[1]
        self.x_bound = curr_stage.x
        self.y_bound = curr_stage.y
        self.curr_stage = curr_stage
        
    def move(self, movement: tuple[int,int]):
        if (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            #update destination
            new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]
            move_tile = self.curr_stage.object_list[new_y][new_x]
            
            #reaction e.g. paved tile
            if "reactive" in tiles.tile_floor_tags[move_tile.tile_floor]:
                move_tile.tile_floor = tiles.tile_reactions[(self.tile_object, move_tile.tile_floor)]
                self.tile_object = None

            #portal
            elif "portal" in tiles.tile_floor_tags[move_tile.tile_floor]:
                animate(self.curr_stage, 0.125)

                #sets portal destination
                destination_portal = self.curr_stage.floor_interactions[move_tile.tile_floor][(new_x, new_y)]
                move_tile = self.curr_stage.object_list[destination_portal[1]][destination_portal[0]]

                #attempt to teleport
                if move_tile.tile_object == None:
                    move_tile.tile_object = self.tile_object
                    self.tile_object = None

            #just move
            elif move_tile.tile_object == None:
                move_tile.tile_object = self.tile_object
                self.tile_object = None

            elif "reactive" in tiles.tile_object_tags[move_tile.tile_object]:
                ...

            #ice
            if "slippery" in tiles.tile_floor_tags[move_tile.tile_floor]:
                animate(self.curr_stage, 0.0625)
                move_tile.move(movement)
            

def display(curr_stage: stage, ASCII:bool):
    mapstr = ""
    for objlist in curr_stage.object_list:
            for obj in objlist:
                if obj.tile_object:
                    if ASCII == True:
                        mapstr += obj.tile_object
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_object]
                else:
                    if ASCII == True:
                        mapstr += obj.tile_floor
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_floor]
            mapstr += "\n"
    return mapstr


if __name__ == "__main__":
    mapstr = ""
    lvl1 = stage("level.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(lvl1.listed_file)