from menu import main_menu, control_menu
import tiles

class player:
    def __init__(self, location: tuple[int, int], items: dict, bounds: tuple[int,int]):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
        self.x_bound = bounds[0]
        self.y_bound = bounds[1]
        self.bounds = self.x_bound, self.y_bound
    
    def move_up(self):
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


    def move(self, direction: str, next_tile: str):
        if tiles.tile[next_tile]:
            ...
        if direction in {"menu", "m", "me", "men"}:
            main_menu()
        elif direction in {"controls", "c", "co", "con", "cont", "contr", "contro", "control"}:
            control_menu()
        else:
            return self.move()
        
        self.coords = self.x_coords, self.y_coords
