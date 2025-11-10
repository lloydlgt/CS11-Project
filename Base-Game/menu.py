import os
import sys
screen_width = 100

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class Menu:
    def __init__(self, prev_screen):
        self.main = self.main_menu
        self.control = self.control_menu
        self.map_select = self.map_selection
        self.prev = prev_screen
    

def death_screen():
    print("Game Over! Try again next time.")
    exit()


def win_screen():
    clear()
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