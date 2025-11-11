tile_floor_tags = {
    #floor tiles
    "." : {"can_move_to", "floor"},

    "~" : {"interactable", "death_on_touch", "can_move_to", "reactive"},

    "_" : {"can_move_to"},
    "!" : {"can_move_to", "brittle", "interactable"},

    #ice
    "I" : {"can_move_to", "slippery"},

    #conveyors
    "^" : {"can_move_to", "conveyor"},
    "v" : {"can_move_to", "conveyor"},
    "<" : {"can_move_to", "conveyor"},
    ">" : {"can_move_to", "conveyor"},

    #portals
    "(" : {"can_move_to", "portal"},
    ")" : {"can_move_to", "portal"},
    "[" : {"can_move_to", "portal"},
    "]" : {"can_move_to", "portal"},
    "{" : {"can_move_to", "portal"},
    "}" : {"can_move_to", "portal"},
    "A" : {"can_move_to", "portal"},
    "B" : {"can_move_to", "portal"},
    "C" : {"can_move_to", "portal"},
    "D" : {"can_move_to", "portal"},
    "E" : {"can_move_to", "portal"},
    "F" : {"can_move_to", "portal"},

    #evil portal
    "Z" : {"can_move_to", "evil"},

    #buttons/levers
    "g" : {"can_move_to", "button"},
    "G" : {"can_move_to", "lever"},
    "h" : {"can_move_to", "button"},
    "H" : {"can_move_to", "lever"},
    "j" : {"can_move_to", "button"},
    "J" : {"can_move_to", "lever"},
    "k" : {"can_move_to", "button"},
    "K" : {"can_move_to", "lever"},

    #gates/doors
    "0" : {"can_move_to", "door_floor"},
    "1" : {"can_move_to", "door_floor"},
    "2" : {"can_move_to", "door_floor"},
    "3" : {"can_move_to", "door_floor"},
}

#add reactive
tile_object_tags = {
    #obj
    "L" : {"you", "object"},
    "T" : {"interactable", "burnable","choppable", "object"},
    "R" : {"interactable", "pushable", "object"},

    #2nd rock for testing
    "r" : {"interactable", "pushable", "object"},

    #one way triggered
    "%" : {"interactable", "burnable", "object"},

    #gates/doors
    "4" : {"gate"},
    "5" : {"gate"},
    "6" : {"gate"},
    "7" : {"gate"},

    #items
    "+" : {"can_move_to", "auto_pickup", "win_condition", "item"},
    "x" : {"can_move_to", "manual_pickup", "item"},
    "*" : {"can_move_to", "manual_pickup", "item"}
    
}

tile_reactions = {
    ("R","~") : "_"
}

#unique interactions i just cram here lol
tile_special = {
    #conveyors
    "^" : (0,-1),
    "v" : (0,1),
    "<" : (-1,0),
    ">" : (1,0),

    "g" : "4",
    "G" : "4",
    "h" : "5",
    "H" : "5",
    "j" : "6",
    "J" : "6",
    "k" : "7",
    "K" : "7",

    "0" : "g",
    "4" : ("g", "0"),

    "1" : "h",
    "5" : ("h", "1"),

    "2" : "j",
    "6" : ("j", "2"),

    "3" : "k",
    "7" : ("k", "3"),
}

translate_tiles = {
    #tiles
    "L":"\N{adult}",
    ".": "  ",
    "T": "\N{evergreen tree}",
    "R": "\N{rock}",
    "~": "\N{large blue square}",
    "_": "\N{White Large Square}",

    #items
    "+": "\N{mushroom}",
    "x": "\N{Axe}",
    "*": "\N{fire}",

    #DLC tiles
    "@": "\N{fire}",

        #2nd rock for testing
    "r" : "🗿",

        #one way
    "!": "\N{Broken Heart}",
    "%": "\N{Wilted Flower}",

        #ice
    "I": "\N{large blue diamond}",

        #conveyors
    "^" : "⏫",
    "v" : "⏬",
    "<" : "⏪",
    ">" : "⏩",
    
        #portals
    "(" : "\N{Aries}",
    ")" : "\N{Taurus}",
    "[" : "\N{Gemini}",
    "]" : "\N{Cancer}",
    "{" : "\N{Leo}",
    "}" : "\N{Virgo}",
    "A" : "\N{Libra}",
    "B" : "\U0000264F",
    "C" : "\N{Sagittarius}",
    "D" : "\N{Capricorn}",
    "E" : "\N{Aquarius}",
    "F" : "\N{Pisces}",

        #evil portal
    "Z" : "\N{Ophiuchus}",

        #supposedly buttons/levers/gates
    "g" : "\U00002660",
    "G" : "\U00002716",

    "h" : "\U00002665",
    "H" : "\U00002795",

    "j" : "\U00002666",
    "J" : "\U00002796",

    "k" : "\U00002663",
    "K" : "\U00002797",

    "0" : "\U0001F315",
    "1" : "\U0001F316",
    "2" : "\U0001F317",
    "3" : "\U0001F314",

    "4" : "\U0001F311",
    "5" : "\U0001F312",
    "6" : "\U0001F313",
    "7" : "\U0001F318",
    
    #dlc items

}

tiles_translate = dict((j,v) for v, j in translate_tiles.items())

print("\U00000030, \U0000FE0F, \U000020E3")