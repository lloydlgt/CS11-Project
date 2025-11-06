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
        |                                |
        |      Please type your map      |
        |                                |
        |      Make sure file is in      |
        |          Maps folder           |
        |                                |
        |          Press Enter           |
        |        for default map         |
        |                                |
        ..................................
        """)
        os.system("dir /b /a-d maps\*.txt") # Prints all the files in the maps subfolder
        self.chosenmap = input("Please type your map: ") 
        #mapList = os.system("dir /b /a-d *.txt")
    


def death_screen():
    print("bitch you cant swim")
    sys.exit()

def win_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print("Congrats, you've finished the game! have a cake :)")
    print("""                  
            /M/              .,-=;//;-
        .:/= ;MH/,    ,=/+%$XH@MM#@:
        -$##@+$###@H@MMM#######H:.    -/H#H
    .,H@H@ X######@ -H#####@+-     -+H###@X
    .,@##H;      +XM##M/,     =%@###@X;-
    X%-  :M##########$.    .:%M###@%:
    M##H,   +H@@@$/-.  ,;$M###@%,          --
    M####M=,,---,.-HHH####M$:          ,+@##
    @##################@/.         :%H##@$-
    M###############H,         ;HM##M$=
    #################.    .=$M##M$=
    ################H..;XM##M$=          .:++
    M###################@%=           =+@MH%
    @#################M/.         =+H#X%=
    =+M###############M,      ,/X#H+:,
    .;XM###########H=   ,/X#H+:;
        .=+HM#######M+/+HM@+=.
            ,:/XMM####H/.
        
    """)
    sys.exit()

if __name__ == "__main__":
    menu = Menu("main")
    x = getattr(menu, "main")
    x()