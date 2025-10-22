tile_tags = {
    #tiles
    "L" : {"you"},
    "." : {"can_move_to"},
    "T" : {"interactable", "burnable","choppable"},
    "R" : {"interactable", "pushable", "cover"},
    "~" : {"interactable", "coverable", "death_on_touch"},
    "_" : {"can_move_to"},

    #items
    "+" : {"can_move_to", "auto_pickup", "win_condition"},
    "x" : {"can_move_to", "manual_pickup"},
    "*" : {"can_move_to", "manual_pickup"}
}

translate_tiles = {
    #tiles
    "L":"\N{adult}",
    ".": "  ",
    "T": "\N{evergreen tree}",
    "R": "\N{rock} ",
    "~": "\N{large blue square}",
    "_": "\N{White Large Square}",
    
    #items
    "+": "\N{mushroom}",
    "x": "\N{Axe}",
    "*": "\N{fire}"
}

tiles_translate = dict((j,v) for v, j in translate_tiles.items())

