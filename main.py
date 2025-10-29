import os
import sys
import time
import tiles
from menu import Menu, win_screen
from mapper import stage
from player import player
#from booter import launch
import controls


menu = Menu("main")
menu.main_menu()

curr_stage = stage(menu.chosenmap) # Make "stage of" string file chosen which redirects to the file the player chooses
print(sys.getsizeof(curr_stage))
#time.sleep(5)
#make this a comprehension for multiple player characters
characters = []
for char_loc in curr_stage.curr_locs:
    characters.append(player(char_loc[0], (curr_stage.x, curr_stage.y), char_loc[1], curr_stage))


while True:
    os.system("cls" if os.name == "nt" else "clear")  
    mapstr = ""
    for objlist in curr_stage.object_list:
        for obj in objlist:
            if obj.tile_object:
                mapstr += obj.tile_object
            else:
                mapstr += obj.tile_floor
        mapstr += "\n"
    print(mapstr)
    print(f"\N{mushroom}: {curr_stage.score}")
    menu.prev = "in_game"
    for char in characters:
        if char.curr_tile != None and "manual_pickup" in tiles.tile_object_tags[tiles.tiles_translate[char.curr_tile]]:
            print("Press P to pick up item:")
            break
    #for loop this later for every character
    #move player
    for indiv_inputs in input("> ").lower():
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")

        #movement
        if indiv_inputs in controls.movement_keybinds: #and map isnt cleared
            #print("passed if moving")
            #time.sleep(2)
            for char in characters:
                #print("moving shit")
                #time.sleep(2)
                movement = getattr(char, "move_" + controls.movement_keybinds[indiv_inputs.lower()])
                char.move(movement(), controls.movement_keybinds[indiv_inputs.lower()])

        #ui
        elif indiv_inputs in controls.ui_keybinds:
            key = getattr(menu, controls.ui_keybinds[indiv_inputs.lower()])
            key()
            break

        #player actions
        elif indiv_inputs in controls.player_action_keybinds:
            for char in characters:
                if char.curr_tile != None and "manual_pickup" in tiles.tile_object_tags[tiles.tiles_translate[char.curr_tile]]:
                    curr_stage.inventory = tiles.tiles_translate[char.curr_tile]
                    char.curr_tile = None

        mapstr = ""
        for objlist in curr_stage.object_list:
            for obj in objlist:
                if obj.tile_object != None:
                    mapstr += obj.tile_object
                else:
                    mapstr += obj.tile_floor
            mapstr += "\n"
        print(mapstr)
        print(f"\N{mushroom}: {curr_stage.score}")
        time.sleep(0.1)
    menu.prev = "in_game"
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
    if curr_stage.score >= curr_stage.score_req:
        win_screen()
        