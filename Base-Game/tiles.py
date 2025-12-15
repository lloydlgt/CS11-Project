# Tile, object, item tags

tile_floor_tags = {
    # Floor tiles
    ".": {"can_move_to", "floor"},
    "~": {"interactable", "death_on_touch", "can_move_to", "floor", "reactive"},
    "_": {"can_move_to", "floor"},
}
"""
Tags:\n
"can_move_to": Valid tile for movement\n
"interactable": Has interactions with other objects\n
"death_on_touch": Kills the player when they step on them\n
"reactive": States that the tile has a reaction when interacted with another specific tile\n
"floor": Tile floor
"""

tile_object_tags = {
    # Objects
    "L": {"you", "object"},
    "T": {"interactable", "burnable", "choppable", "object"},
    "R": {"interactable", "pushable", "object"},

    # Items
    "+": {"can_move_to", "auto_pickup", "win_condition", "item"},
    "x": {"can_move_to", "manual_pickup", "item"},
    "*": {"can_move_to", "manual_pickup", "item"},
}
"""
Tags:\n
"you": You, the player\n
"can_move_to": Valid tile for movement\n
"auto_pickup": Is automatically picked up when the player steps on it\n
"manual_pickup": Requires an input to be picked up\n
"win_condition": The Mushroom\n
"object": Tile object\n
"item": Item
"""

tile_reactions = {
    # Paved tile, rock -> water
    ("R", "~"): "_"
}
"""
Rock + Water = Paved Tile
"""
# Tile and item UI representations
translate_tiles = {
    # Tiles
    "L": "\N{adult}",
    ".": "\u3000",
    "T": "\N{evergreen tree}",
    "R": "\N{rock} ",
    "~": "\N{large blue square}",
    "_": "\N{White Large Square}",

    # Items
    "+": "\N{mushroom}",
    "x": "\N{Axe}",
    "*": "\N{fire}",
}
"""
Turns the ASCII tile into an Emoji (like the movie) (They made 2 of them)
"""
