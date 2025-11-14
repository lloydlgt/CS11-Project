import tiles
from player import character


class stage():
    def __init__(self, path):
        self.path = path

    def start(self):
        try:
            # Setup the map variables and insure actual dimensions match initialized forest dimensions
            with open(self.path, "r") as file:
                self.file = file
                self.read_lines = self.file.readlines()
                self.y, self.x = (int(num) for num in self.read_lines[0].split(" "))
                self.listed_file = list(x.rstrip() for x in self.read_lines[1:])

                if any((self.y != len(self.listed_file), self.x != len(self.listed_file[0]))): # Insurance for grid dimensions
                    print(f"Error: Initialized forest dimension {self.y}, {self.x} does not match actual forest dimension {len(self.listed_file)}, {len(self.listed_file[0])}.")
                    exit()        
        except FileNotFoundError:
            # Handles inputting a non-existent stage file
            print(f"Error: Stage file {self.path} not found.")
            exit()

        # Game stats
        self.score = 0
        self.score_req = 0
        self.inventory = None
        self.object_list = list([0,] * self.x for y in range(self.y))
        self.curr_locs = [] 
        self.character = () 

        # "Load" up the main map
        for y in range(self.y):
            for x in range(self.x):

                if self.listed_file[y][x] == "+":
                    self.score_req += 1

                # Save the character ("Laro")'s position
                if self.listed_file[y][x] == "L":
                    self.character = character((x,y),(self.x,self.y), None, self)

                # Creates tile object
                self.object_list[y][x] = stage_tile(None, ".", (x,y), self)

                # If tile is on top layer, set it to top layer
                if self.listed_file[y][x] in tiles.tile_object_tags:
                    self.object_list[y][x].tile_object = self.listed_file[y][x]

                # If tile is on floor layer, set it to bottom layer
                elif self.listed_file[y][x] in tiles.tile_floor_tags:
                    self.object_list[y][x].tile_floor = self.listed_file[y][x]
    



class stage_tile:
    """Individual Stage Tile that holding"""
    
    # Optimization for memory usage by locking the class to only have these attributes and nothing else

    __slots__ = ("tile_object", "tile_floor", "x_coords", "y_coords", "x_bound", "y_bound", "curr_stage")

    # Initializes each stage tile as their own object
    def __init__(self, tile_object: str, tile_floor: str, coords: tuple[int,int], curr_stage: stage):
        # Tile object is the top layer of the tile
        # Tile floor is the bottom layer of the tile     
        self.tile_object = tile_object
        self.tile_floor = tile_floor
        self.x_coords, self.y_coords = coords[0], coords[1]
        self.x_bound = curr_stage.x
        self.y_bound = curr_stage.y
        self.curr_stage = curr_stage
        
    def move(self, movement: tuple[int,int]):
        """Moves the object currently on this tile
        Args:
            movement: Movement direction as a tuple (x,y)
        """
        # Check if movement is valid i.e. within the boundary
        if (0 <= self.y_coords + movement[1] < self.y_bound and 0 <= self.x_coords + movement[0] < self.x_bound):
            # Sets the reference for tile to move to
            new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]
            move_tile = self.curr_stage.object_list[new_y][new_x]
            
            # Check if the tile object and the floor of the tile being moved to have a reaction
            if "reactive" in tiles.tile_floor_tags[move_tile.tile_floor]:
                move_tile.tile_floor = tiles.tile_reactions[(self.tile_object, move_tile.tile_floor)]
                self.tile_object = None

            # Check if the next tile is empty and move the tile object
            elif move_tile.tile_object == None:
                move_tile.tile_object = self.tile_object
                self.tile_object = None


def display(curr_stage: stage, ASCII: bool):
    # To display the current state of the map in one function for reusability and readability

    mapstr = ""
    for objlist in curr_stage.object_list:
            for obj in objlist:
                if obj.tile_object:
                    if ASCII:
                        mapstr += obj.tile_object
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_object]
                else:
                    if ASCII:
                        mapstr += obj.tile_floor
                    else:
                        mapstr += tiles.translate_tiles[obj.tile_floor]
            mapstr += "\n"
    return mapstr


if __name__ == "__main__":
    mapstr = ""
    lvl1 = stage("default.txt")
    for row in lvl1.maplist:
        mapstr += "".join(row) + "\n"
    print(lvl1.listed_file)