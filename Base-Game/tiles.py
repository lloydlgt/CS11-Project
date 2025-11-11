# Tile, object, item tags
tile_floor_tags = {
    # Floor tiles
    "." : {"can_move_to", "floor"},
    "~" : {"interactable", "death_on_touch", "can_move_to", "floor", "reactive"},
    "_" : {"can_move_to", "floor"},
}

tile_object_tags = {
    # Objects
    "L" : {"you", "object"},
    "T" : {"interactable", "burnable","choppable", "object"},
    "R" : {"interactable", "pushable", "object"},

    # Items
    "+" : {"can_move_to", "auto_pickup", "win_condition", "item"},
    "x" : {"can_move_to", "manual_pickup", "item"},
    "*" : {"can_move_to", "manual_pickup", "item"},
}

tile_reactions = {
    ("R","~") : "_"
}

# Tile and item UI representations
translate_tiles = {
    # Tiles
    "L":"\N{adult}",
    ".": "  ",
    "T": "\N{evergreen tree}",
    "R": "\N{rock}",
    "~": "\N{large blue square}",
    "_": "\N{White Large Square}",

    # Items
    "+": "\N{mushroom}",
    "x": "\N{Axe}",
    "*": "\N{fire}",
}
