from menu import main_menu, control_menu

class player:
    def __init__(self, location: tuple[int, int], items: dict):
        self.x_coords = location[0]
        self.y_coords = location[1]
        self.coords = self.x_coords, self.y_coords
    
    def move(self, direction: str):
        direction = direction.lower()
        if direction == "w":
            self.y_coords -= 1
        elif direction == "s":
            self.y_coords += 1
        elif direction == "a":
            self.x_coords -= 1
        elif direction == "d":
            self.x_coords += 1
        elif direction in {"menu", "m", "me", "men"}:
            main_menu()
        elif direction in {"controls", "c", "co", "con", "cont", "contr", "contro", "control"}:
            control_menu()
        else:
            return self.move()
        
        self.coords = self.x_coords, self.y_coords
