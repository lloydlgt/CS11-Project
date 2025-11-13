import os
import sys
import time
from mapper import stage
import tiles


class Menu:
    "holds the screens"
    # Initialize the menu and the original map when the user inputs map reset
    def __init__(self):
        self.reset = self.reset_menu
        self.prev_map = ""
        self.curr_stage = None
    
    def reset_menu(self):
        "resets the map"
        self.curr_stage = stage(self.prev_map)
        self.curr_stage.start()

    
def win_screen():
    "The win screen once all mushroom has been collected"
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
    exit()


if __name__ == "__main__":
    menu = Menu("main")
    x = getattr(menu, "main")
    x()