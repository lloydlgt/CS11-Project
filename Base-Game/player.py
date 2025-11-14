import os
import tiles
import controls

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def input_handler(movement_string, curr_stage):
     for indiv_input in movement_string.lower():
        validated_input = curr_stage.character.run_input(indiv_input)
        if not validated_input:
            break
        if validated_input == "dead":
            break
        if curr_stage.score >= curr_stage.score_req:
            break

class character:

    # Initializes the character with its positions, boundaries, current tile, and current stage

    def __init__(self, location: tuple[int, int], bounds: tuple[int,int], curr_tile: str, curr_stage):
        """
            location: Player location as tuple (x,y)
            bounds: Boundaries of map as tuple (x,y)
            curr_tile: Tile that player is currently standing on
            curr_stage: Reference to the current stage
        """
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.curr_tile = curr_tile
        self.curr_stage = curr_stage
    
    def move(self, movement: tuple[int,int]):
        """ Main function that checks what happens when the character moves
        Args:
            movement: Movement direction as tuple (x,y)
        """
        # Coordinates of the next position
        new_x,new_y = self.x_coords + movement[0], self.y_coords + movement[1]

        # If out of bounds, do nothing
        if not (0 <= new_y < self.y_bound and 0 <= new_x < self.x_bound):
<<<<<<< HEAD
            return True
=======
            return "out of bounds"
>>>>>>> 1414a76ac0e3fd94a4ad6d2e88fdcc3c980e9d2f

        # Checks what the next tile is and its tags (descriptions)
        next_tile = self.curr_stage.object_list[new_y][new_x]
        next_tile_floor_tags = tiles.tile_floor_tags[next_tile.tile_floor]

        # If the next tile is an object (tree/rock), get its tags
        if next_tile.tile_object:
            next_tile_object_tags = tiles.tile_object_tags[next_tile.tile_object]
        else:
            next_tile_object_tags = {}

        # If the next tile is interactable (i.e., it's pushable, choppable, or burnable)
        if "interactable" in next_tile_object_tags:

            # If it's pushable, run the move function for the rock
            if "pushable" in next_tile_object_tags:
                next_tile.move(movement)
            
            # If it's choppable, check if you have an axe or not 
            if "choppable" in next_tile_object_tags:
                if self.curr_stage.inventory in {"x"}:
                    # "Chop" the tree down
                    self.curr_stage.object_list[new_y][new_x].tile_object = None
                    self.curr_stage.inventory = None

            # If it's burnable, check if you have a flamethrower or not
            if "burnable" in next_tile_object_tags:
                if self.curr_stage.inventory in {"*"}:
                    # Create a set containing the first tree to burn
                    burn = {(new_x, new_y)}

                    # All adjacent directions
                    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

                    # While there are trees to burn
                    while burn:
                        # Creates fire and makes a copy for adjacent trees
                        temp_burn = burn.copy()

                        # "Burns" all the trees
                        for trees in burn:
                            self.curr_stage.object_list[trees[1]][trees[0]].tile_object = None
                        burn.clear() 

                        # Checks adjacent cells for trees
                        for trees in temp_burn:
                            for direction in directions:
                                if 0 <= trees[0] + direction[0] < self.x_bound and 0 <= trees[1] + direction[1] < self.y_bound:
                                    if self.curr_stage.object_list[trees[1] + direction[1]][trees[0] + direction[0]].tile_object and "burnable" in tiles.tile_object_tags[self.curr_stage.object_list[trees[1] + direction[1]][trees[0] + direction[0]].tile_object]:
                                        burn.add((trees[0] + direction[0], trees[1] + direction[1]))
                    self.curr_stage.inventory = None            

        next_tile = self.curr_stage.object_list[new_y][new_x]
        next_tile_floor_tags = tiles.tile_floor_tags[next_tile.tile_floor]

        if next_tile.tile_object:
            next_tile_object_tags = tiles.tile_object_tags[next_tile.tile_object]
        else:
            next_tile_object_tags = {}

        # If the next tile is a tile the character can move to
        if "can_move_to" in next_tile_floor_tags:
            # If the next tile is not an object (empty/water)
            if not next_tile_object_tags:
                # Move the character to the next tile
                next_tile.tile_object = "L"
                self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                self.curr_tile = None
                self.x_coords, self.y_coords = new_x, new_y
                if "death_on_touch" in next_tile_floor_tags:
                    # If the character falls in water, display death screen and end game
                    self.curr_stage.object_list[self.y_coords][self.x_coords].tile_object = self.curr_tile
                    return False

            # If the next tile is an item
            elif "item" in next_tile_object_tags:
                # If the next tile is automatically collected (mushroom)
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
        return True

    def run_input(self, indiv_input: str):
        """ Runs each individual input
        Args:
            indiv_input: Individual input
        """
        if indiv_input == "!":
            self.curr_stage.reset
            return "reset"
        if indiv_input not in (controls.movement_keybinds | controls.player_action_keybinds):
            return False
        # Player movement
        if indiv_input in controls.movement_keybinds:
            moved = self.move(controls.movement_keybinds[indiv_input.lower()])
            if not moved:
                return "dead"
        # Player interactions
        elif indiv_input in controls.player_action_keybinds:
            if not self.curr_stage.inventory and self.curr_tile and "manual_pickup" in tiles.tile_object_tags[self.curr_tile]:
                self.curr_stage.inventory = self.curr_tile
                self.curr_tile = None

        return True
  
if __name__ == "__main__":
    print("Wrong file.")
