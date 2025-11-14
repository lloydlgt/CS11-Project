import os
import sys
import time
import tiles
from mapper import stage



class Menu:
    def __init__(self, prev_screen):
        self.reset = self.reset_menu
        self.main = self.main_menu
        self.control = self.control_menu
        self.map_select = self.map_selection
        self.prev = prev_screen
        self.prev_map = ""
        self.curr_stage = None
        self.storymode = False
        self.maps = []
    
    def main_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("""\33[91;1m
██████╗  ██████╗  ███████╗ ████████╗ ███████╗ ███████╗ ███████╗ ██╗    
██╔══██╗ ██╔══██╗ ██╔══██║ ╚══██╔══╝ ██╔══██║ ██╔════╝ ██╔══██║ ██║    
██████╔╝ ██████╔╝ ██║  ██║    ██║    ██║  ██║ ██║      ██║  ██║ ██║
██╔═══╝  ██╔══██╗ ██║  ██║    ██║    ██║  ██║ ██║      ██║  ██║ ██║
██║      ██║  ██║ ███████║    ██║    ███████║ ╚██████╗ ███████║ ╚██████╗    
╚═╝      ╚═╝  ╚═╝ ╚══════╝    ╚═╝    ╚══════╝  ╚═════╝ ╚══════╝  ╚═════╝   
            ██████╗  ███████╗  ██████╗   █████╗ 
            ╚════██╗ ██╔════╝ ██╔═████╗ ██╔══██╗
            █████╔╝  ███████╗ ██║██╔██║ ╚█████╔╝
            ██╔═══╝  ╚════██║ ████╔╝██║ ██╔══██╗
            ███████╗ ███████║ ╚██████╔╝ ╚█████╔╝
            ╚══════╝ ╚══════╝  ╚═════╝   ╚════╝ 
\33[0m""")

        print("""\33[90m───────────────────────────────────────────────────────────────
                   PROJECT:  [███████ RECURSION SEROQUEL]
                   STATUS :  ACTIVE
                   SUBJECT:  ██-███████
───────────────────────────────────────────────────────────────\33[0m""")

        print("""\33[96m
  [1] CHOOSE DESTINATION
  [2] FOLLOW YOUR DESTINY
  [3] LEARN YOURSELF
  [4] TERMINATE SESSION
\33[0m""")

        print("""\33[91;1m
WARNING: DO NOT LOSE YOURSELF.
REMEMBER YOUR GOAL.
\33[95;1m""")
        self.player_input = input("> ").lower()
        print("\33[0m")
        if self.player_input == "1":
            os.system("cls" if os.name == "nt" else "clear")
            self.map_selection()
        elif self.player_input == "2":
            self.storymode = True
        elif self.player_input == "3":
            self.control_menu()
        elif self.player_input == "4":
            sys.exit()
        else:
            self.main_menu()

    def control_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("""\33[97;1m
████████████████████████████████████████████████
█                                              █
█              █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█              █
█              █  CONTROL MENU  █              █
█              █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█              █
█                                              █
█                                              █
█     YOUR ACTIONS:                            █
█     \33[0m    \33[96mW - MOVE UP     \33[97;1m                     █
█      \33[0m   \33[96mA - MOVE LEFT   \33[97;1m                     █
█      \33[0m   \33[96mS - MOVE DOWN   \33[97;1m                     █
█      \33[0m   \33[96mD - MOVE RIGHT  \33[97;1m                     █
█      \33[0m   \33[96mP - PICKUP ITEM \33[97;1m                     █
█                                              █
█      AVAILABLE COMMANDS:                     █
█    \33[0m     \33[95m! - RESET MAP          \33[97;1m              █
█     \33[0m    \33[95mM - RETURN TO MAIN MENU\33[97;1m              █
█     \33[0m    \33[95mC - VIEW CONTROLS      \33[97;1m              █
█                                              █
█                                              █
█                                              █
█  \33[91;1mWARNING: UNAUTHORIZED ACCESS WILL BE\33[97;1m        █
█           \33[91;1mLOGGED AND REPORTED\33[97;1m                █
█                                              █
█                                              █
████████████████████████████████████████████████
        \33[0m""")
        input("Press Enter to go back...")
        if self.prev == "main":
            self.prev = "main"
            self.main_menu()


    def map_selection(self):
        print("")
        os.system("dir /b /a-d DLC\maps\*.txt") # Prints all the files in the maps subfolder
        self.chosenmap = input("Please type your map: ")
        self.curr_stage = stage(self.chosenmap)
        if not self.chosenmap:
            self.prev_map = "default.txt"
        else:
            self.prev_map = self.chosenmap
        self.curr_stage.start()
        #mapList = os.system("dir /b /a-d *.txt")
    
    def reset_menu(self):
        print(f"[DEBUG] Reset called | prev_map: {self.prev_map}")
        if not self.prev_map:
            print("No previous map to reset.")
            return
        self.curr_stage = stage(self.prev_map)
        self.curr_stage.start()

    
    

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