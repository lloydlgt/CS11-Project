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
    "m" : {"can_move_to", "button"},
    "M" : {"can_move_to", "lever"},
}

#add reactive
tile_object_tags = {
    #obj
    "L" : {"you", "object"},
    "T" : {"interactable", "burnable","choppable", "object"},
    "R" : {"interactable", "pushable", "object"},

    #one way triggered
    "%" : {"interactable", "burnable", "object"},

    #gates/doors
    "0" : {"gate"},
    "1" : {"gate"},
    "2" : {"gate"},
    "3" : {"gate"},
    "4" : {"gate"},

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
    "^" : (0,-1),
    "v" : (0,1),
    "<" : (-1,0),
    ">" : (1,0),
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
    "*": "\N{fire}",

    #DLC tiles
    "@": "\N{fire}",

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
    "Z" : "\N{Ophiuchus}"

        #supposedly buttons/levers/gates
    #"g" :
    #"G" :
    #"h" :
    #"H" :
    #"j" :
    #"J" :
    #"k" :
    #"K" :
    #"m" :
    #"M" :
#
    #"0" :
    #"1" :
    #"2" :
    #"3" :
    #"4" :
    #DLC items

}

tiles_translate = dict((j,v) for v, j in translate_tiles.items())
