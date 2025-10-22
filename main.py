import os
import sys
import time
import tiles
from menu import Menu
from mapper import stage
from player import player
#from booter import launch
import controls


menu = Menu("main")
menu.main_menu()
curr_stage = stage("est.txt")

#make this a comprehension for multiple player characters
characters = []
for char_loc in curr_stage.curr_locs:
    characters.append(player(char_loc[0], (curr_stage.x, curr_stage.y), char_loc[1], curr_stage))


while True:
    os.system("cls" if os.name == "nt" else "clear")
    mapstr = ""
    for row in curr_stage.maplist:
        mapstr += "".join(row) + "\n"
    print(mapstr)
    print(f"\N{mushroom}: {curr_stage.score}")
    menu.prev = "in_game"
    if "manual_pickup" in tiles.tile_tags[tiles.tiles_translate[characters[0].curr_tile]]:
        print("Press P to pick up item:")
    #for loop this later for every character
    #move player
    for indiv_inputs in input("> ").lower():
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")

        #movement
        if indiv_inputs in controls.movement_keybinds: #and map isnt cleared
            for char in characters:
                movement = getattr(char, "move_" + controls.movement_keybinds[indiv_inputs.lower()])
                rech = char.move(movement())
                char.rewind(rech)

        #ui
        elif indiv_inputs in controls.ui_keybinds:
            key = getattr(menu, controls.ui_keybinds[indiv_inputs.lower()])
            key()
            break

        #player actions
        elif indiv_inputs in controls.player_action_keybinds:
            if "manual_pickup" in tiles.tile_tags[tiles.tiles_translate[characters[0].curr_tile]]:
                char.items = tiles.tiles_translate[characters[0].curr_tile]
                char.curr_tile = "  "

        mapstr = ""
        for row in curr_stage.maplist:
            mapstr += "".join(row) + "\n"
        print(mapstr)
        print(f"\N{mushroom}: {curr_stage.score}")
    """time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    print(
                                                                                                
                                                                                                
                                                                                                
                                      ░░░▓▓▓▓▒░░░                                               
                                    ░▒██████████▓                                               
                                  ░▒████▓▓█▓░▒▒░░░░░                                            
                                    ░██▒░▒▒░▒▒▒▒▒░▒░                                             
                                    ░░▒▓▓▒▒░░▒▒▒▒▒░░                                            
                                    ░▒▒▒░░░░▒░▒▒░░░░░                                           
                                      ░▒▒██▓░▒▒▓▓▓▓▓▓▓░                                          
                                      ░▓▒▒░░▒▓▓▓▓▓▓▓▓▓▒░░                                       
                                      ░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░                                   
                        ░░░░░░░░░░░ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░                                
                      ░▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                               
                    ░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░░                        
                    ░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░                     
                    ░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░                    
                    ░░░░▒░░░░░░▒░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░                   
                    ░░▒░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░                  
                    ▒░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░                  
                    ░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▒░                  
                ░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░                  
            ░░▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░                
            ░▓█▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▒░░░░░▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░               
          ░▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▒░░░░░░░░░░▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░              
          ░▓█▓▓▓▒▒▒▒▒▓██▓▓▓████▓▓▓▓▓▓▓▓▓█████▓░░░░▒▒░▒▒▒▒▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓░             
          ▒▓░▒▓▒░░░░░▒▒▒▒▒▓███████████████▓▓░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▓▓▓▓▓▓▒░░▒▒▒░▒░░▓▓░░            
          ░░▒▓▓▓▒░░░░░░░░░▒██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░      ░█▒▒░░░░░░▒░░▒░ ░▒▒░            
          ▒▓▒▓▓▓▓▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░      ░█▓░░░░░░░░░▒▒░░ ░░             
          ░▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▒▒▒░░░░░▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓█▓▓▓▓▓▓▓▓▓▒▒░░░▓█▓▒░░░░░░▒▒▓▒░                
          ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓░                  
        ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓░                    
        ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓░                     
      ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                    
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░                  
      ▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                 
      ▒█▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓                  
      ░█▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▓▓▓                  
        ▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░▒▓▓▓▓▒                  
        ░▓▓▓▓▓▓▓▓▓▒░░░░░░░░░▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▓▓░░                  
          ░▓▓▓▓▓▓▓▒░░░░░░░░░░░░░▒▒▒▓█▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓█▓░░░░░░░░                    
            ░░▓▓▓▓░░░░░░░░░░░░░░░░░▒▒▓███████████▒░░▓█████████████▓▒░░░░▒░░                      
              ░░▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▒░░░░  ░▒▒▓███████▓▒░░░░░░░░                        
                ░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▒░░░░░░░▒▒▒▒▒░    ░▒▒▒▒▒▒▒▒▒░░░░░░░░░                           
                                ░░░░░░░▒▒▒▒▒▒░    ░▒▒▒▒▒▒▒▒░░░░▒░░                              
                                ░░░░░░▒▒▒▒▒▒▒░    ░▒▒▒▒▒▒▒▒░░░░░░                               
                                  ░░░░▒▒▒▒▒▒▒░░     ░▒▒▒▒▒▒▒▒░░░░░░                              
                                ░░░░░▒▒▒▒▒▒░        ░▒▒▒▒▒▒▒▒░░░░░░                             
                            ░░░░░░░░░▒▒▒▒▒▒░           ░▒▒▒▒▒▒▒░░░░░░░░                          
                          ░░░░░░░░░░▒▒▒▒▒▒░             ░▒▒▒▒▒▒▒▒░░░░░░░                         
                          ░░░░░░░░▒▒▒▒▒▒▒▒░              ░▒▒▒▒▒▒▒▒▒▒▒▒░▒░                        )
time.sleep(12)
"""
    if curr_stage.score >= curr_stage.indiv_char.count("+"):
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
                ,.:=-.
    """)
        break