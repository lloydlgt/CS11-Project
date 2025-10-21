import os
import sys
screen_width = 100

class Menu:
    def __init__(self, prev_screen):
        self.main = self.main_menu
        self.control = self.control_menu
        self.map_select = self.map_selection
        self.prev = prev_screen
    
    def main_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
        ----------------------------------------
        |                                      |
        |      Put the fries in the bag        |
        |                                      |
        |                                      |
        |                Play                  |
        |              Controls                |
        |                Quit                  |
        ----------------------------------------
        """)
        self.player_input = input("> ").lower()
        if self.player_input in ("play", "p", "pl", "pla"):
            os.system("cls" if os.name == "nt" else "clear")
            self.map_selection()
        elif self.player_input in ("controls", "c", "co", "con", "cont", "contr", "contro", "control"):
            self.control_menu()
        elif self.player_input in ("quit", "q", "qu", "qui"):
            sys.exit()
        else:
            self.main_menu()

    def control_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("""
        ..................................
        .            Controls:           .
        .                                .
        .         W - Move up            .
        .         A - Move left          .
        .         S - Move down          .
        .         D - Move right         .
        .         P - Pick up item       .
        .         ! - Reset map          .
        .                                .
        ..................................
        """)
        input("Press Enter to go back...")
        if self.prev == "main":
            self.prev = "main"
            self.main_menu()


    def map_selection(self):
        print("""
        ..................................
        .                                .
        .                                .
        .                                .
        .          type you map          .
        .                                .
        .                                .
        .                                .
        .                                .
        .                                .
        ..................................
        """)
        os.system("dir /b /a-d *.txt")
        theInput = input("type yo map name or else: ")
        #mapList = os.system("dir /b /a-d *.txt")

if __name__ == "__main__":
    menu = Menu("main")
    x = getattr(menu, "main")
    x()