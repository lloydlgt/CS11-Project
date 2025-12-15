import pytest
from mapper import stage, display

# ("Path of map file", "multi-line string of the map", (x_bound, y_bound), (player_x, player_y), mushroom_count)

MAP_ATTRIBUTES = [
    ("default.txt",
        """TTTTTTTTTTTT
T.R.~T+~..+T
T.~.TRTT~T.T
T*.Tx~.RTTRT
T~TTT.T..xTT
T..RT.RTT..T
TTT.TT...T.T
T~...TTTTRTT
TT...RL.T~xT
TR.xT..~.R.T
TTTTTTTTTTTT
""", (11, 12), (8, 6), 2),
    ("map.txt",
        """TTTTTTTTT
T...+...T
T...~...T
T...R.T.T
T.T.TTT.T
T.x..T*.T
T.*.T...T
T..TTTT.T
T.L..T..T
T...T...T
T.TTTT..T
T..*T...T
TTTTTTTTT
""", (13, 9), (8, 2), 1),
    ("mapper_tests/map_1.txt",
        """TTTTTTTTT
T...+...T
T...~...T
T...R.T.T
T.T.LTT.T
T.x...*.T
T.......T
T.......T
TTTTTTTTT
""", (9, 9), (4, 4), 1),
    ("mapper_tests/map_2.txt",
        """+++
+++
++L
""", (3, 3), (2, 2), 8),
    ("mapper_tests/map_3.txt",
        """TTTTT
T..+T
T...T
TL..T
TTTTT
""", (5, 5), (3, 1), 1),
    ("mapper_tests/map_4.txt",
        """TTTTT
T~~+T
T...T
TL~~T
TTTTT
""", (5, 5), (3, 1), 1),
    ("mapper_tests/map_5.txt",
        """TTTTTTT
T~~~+~T
T..R..T
TL~~~~T
TTTTTTT
""", (5, 7), (3, 1), 1),
    ("mapper_tests/map_6.txt",
        """TTTTTTTTTTTTTTTTTTTTTTTTTTTTTL
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
T............................T
+++++++......................T
+++++++......................T
+++++++TTTTTTTTTTTTTTTTTTTTTTT
""", (30, 30), (0, 29), 21),
    ("mapper_tests/map_7.txt",
        """TTTTT
TL..T
T.R.T
T...T
T~~~T
T.+.T
TTTTT
""", (7, 5), (1, 1), 1),
    ("mapper_tests/map_8.txt",
        """TTTTTTTT
T~LR..~T
T~R~~..T
T..~+~.T
T..~~~.T
T.~R...T
TTTTTTTT
""", (7, 8), (1, 2), 1),
    ("mapper_tests/map_9.txt",
        """TTTTTTTTT
T+.....+T
T~~~~~~~T
T.R.T.R.T
TR.RLR.RT
T.R.T.R.T
T~~~~~~~T
T+.....+T
TTTTTTTTT
""", (9, 9), (4, 4), 4),
    ("mapper_tests/map_10.txt",
        """TTTTTTT
T..T..T
T.R..LT
T.~..TT
Tx..*.T
TTTTTTT
""", (6, 7), (2, 5), 0),
    ("mapper_tests/map_11.txt",
        """TTTTTTTTT
TRT...R.T
TTT.TTR.T
TL.R.T..T
TTTR+~T.T
T..R~~R.T
T..TTTR.T
TR~.....T
TTTTTTTTT
""", (9, 9), (3, 1), 1),
    ("mapper_tests/map_12.txt",
        """TTTTTTTTT
TL.R..~~T
T.RRR~~~T
TR..~~~RT
T..~~~..T
TR~~~RR.T
T~~~...~T
T~~RRR~+T
TTTTTTTTT
""", (9, 9), (1, 1), 1),
    ("mapper_tests/map_13.txt",
        """TTTTTTTTTTT
T.T.~.....T
T.~RT.T.T.T
T~R.T...R.T
TRT.T.T~T.T
T~.TT~R.T.T
TTRRT.TRT.T
T+~TT.R~TLT
TTTTTTTTTTT
""", (9, 11), (7, 9), 1),
    ("mapper_tests/map_14.txt",
        """++++++
++++++
++L+++
""", (3, 6), (2, 2), 17),
    ("mapper_tests/map_15.txt",
        """TTTTTTTTTTT
T.........T
T~RL......T
TRTTT~TTT.T
T...T+T...T
T.R.TRT.TTT
T.......~+T
TTT....R..T
TT~~...TTTT
T+.T......T
TTTTTTTTTTT
""", (11, 11), (2, 3), 3),
    ]


@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    """Create an instance of the stage and return references of each stage attribute

    :param request: Map from list of maps
    :type request: _type_
    :return: Each of the stage's attributes
    :rtype: _type_
    """
    map_file, stage_grid, stage_bounds, character_pos, score_req = request.param
    map = stage(map_file)
    return map, stage_grid, stage_bounds, character_pos, score_req


def test_start(map_stage):
    """Test the boundaries of the stage, starting position of the player, and number of mushrooms to be collected

    :param map_stage: The stage itself
    :type map_stage: _type_
    """
    map, stage_grid, stage_bounds, character_pos, score_req = map_stage
    map.start()
    assert (map.y, map.x) == stage_bounds
    assert (map.character.y_coords, map.character.x_coords) == character_pos
    assert map.score_req == score_req


def test_display(map_stage):
    """Test the ASCII representation of the stage

    :param map_stage: The stage itself
    :type map_stage: _type_
    """
    map, stage_grid, stage_bounds, character_pos, score_req = map_stage
    map.start()
    assert display(map, True) == stage_grid
