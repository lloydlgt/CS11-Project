tile_floor_tags = {
    #floor tiles
    "." : {"can_move_to", "floor"},
    "~" : {"interactable", "death_on_touch", "can_move_to", "floor", "reactive"},
    "_" : {"can_move_to", "floor"},
    "!" : {"can_move_to", "brittle", "interactable"},
    "%" : {"can_move_to", "death_on_touch"}
}

#add reactive
tile_object_tags = {
    #obj
    "L" : {"you", "object"},
    "T" : {"interactable", "burnable","choppable", "object"},
    "R" : {"interactable", "pushable", "object"},

    #items
    "+" : {"can_move_to", "auto_pickup", "win_condition", "item"},
    "x" : {"can_move_to", "manual_pickup", "item"},
    "*" : {"can_move_to", "manual_pickup", "item"}
    
}

tile_reactions = {
    ("R","~") : "_"
}

translate_tiles = {
    #tiles
    "L":"\N{adult}",
    ".": "  ",
    "T": "\N{evergreen tree}",
    "R": "\N{rock} ",
    "~": "\N{large blue square}",
    "_": "\N{White Large Square}",
    "!": "\N{Broken Heart}",
    "%": "\N{Wilted Flower}",
    
    #items
    "+": "\N{mushroom}",
    "x": "\N{Axe}",
    "*": "\N{fire}",

    #DLC tiles
    "@": "\N{fire}",
    #DLC items

}

tiles_translate = dict((j,v) for v, j in translate_tiles.items())

