import os

movement_keybinds = {
    # Move up
    "w" : (0,-1),

    # Move down
    "s" : (0,1),
    
    # Move left
    "a" : (-1,0),

    # Move right
    "d" : (1,0),

}

player_action_keybinds = {
    # Player pickup
    "p" : "pickup",
}

ui_keybinds = {
    # For UI
    "!": "reset"
}

print(os.listdir("maps"))