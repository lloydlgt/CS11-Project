import pytest
from mapper import stage, display

MAP_ATTRIBUTES = [
    ("default.txt", "TTTTTTTTTTTT\nT.R.~T+~..+T\nT.~.TRTT~T.T\nT*.Tx~.RTTRT\nT~TTT.T..xTT\nT..RT.RTT..T\nTTT.TT...T.T\nT~...TTTTRTT\nTT...RL.T~xT\nTR.xT..~.R.T\nTTTTTTTTTTTT\n", (11, 12), (8, 6), 2), 
    ("map.txt", "TTTTTTTTT\nT...+...T\nT...~...T\nT...R.T.T\nT.T.TTT.T\nT.x..T*.T\nT.*.T...T\nT..TTTT.T\nT.L..T..T\nT...T...T\nT.TTTT..T\nT..*T...T\nTTTTTTTTT\n", (13, 9), (8, 2), 1), 
    ("mapper_tests/map_1.txt","TTTTTTTTT\nT...+...T\nT...~...T\nT...R.T.T\nT.T.LTT.T\nT.x...*.T\nT.......T\nT.......T\nTTTTTTTTT\n",(9, 9), (4, 4), 1),
    ("mapper_tests/map_2.txt","+++\n+++\n++L\n",(3, 3), (2, 2), 8),
    ("mapper_tests/map_3.txt", "TTTTT\nT..+T\nT...T\nTL..T\nTTTTT\n",(5, 5), (3, 1), 1),
    ("mapper_tests/map_4.txt", "TTTTT\nT~~+T\nT...T\nTL~~T\nTTTTT\n",(5, 5), (3, 1), 1),
    ("mapper_tests/map_5.txt", "TTTTTTT\nT~~~+~T\nT..R..T\nTL~~~~T\nTTTTTTT\n",(5, 7), (3, 1), 1),
    ("mapper_tests/map_6.txt", "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTL\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\nT............................T\n+++++++......................T\n+++++++......................T\n+++++++TTTTTTTTTTTTTTTTTTTTTTT\n",(30, 30), (0, 29), 21),
    ("mapper_tests/map_7.txt", "TTTTT\nTL..T\nT.R.T\nT...T\nT~~~T\nT.+.T\nTTTTT\n",(7, 5), (1, 1), 1),
    ("mapper_tests/map_8.txt", "TTTTTTTT\nT~LR..~T\nT~R~~..T\nT..~+~.T\nT..~~~.T\nT.~R...T\nTTTTTTTT\n",(7, 8), (1, 2), 1),
    ("mapper_tests/map_9.txt", "TTTTTTTTT\nT+.....+T\nT~~~~~~~T\nT.R.T.R.T\nTR.RLR.RT\nT.R.T.R.T\nT~~~~~~~T\nT+.....+T\nTTTTTTTTT\n",(9, 9), (4, 4), 4),
    ("mapper_tests/map_10.txt", "TTTTTTT\nT..T..T\nT.R..LT\nT.~..TT\nTx..*.T\nTTTTTTT\n",(6, 7), (2, 5), 0),
    ("mapper_tests/map_11.txt", "TTTTTTTTT\nTRT...R.T\nTTT.TTR.T\nTL.R.T..T\nTTTR+~T.T\nT..R~~R.T\nT..TTTR.T\nTR~.....T\nTTTTTTTTT\n",(9, 9), (3, 1), 1),
    ("mapper_tests/map_12.txt", "TTTTTTTTT\nTL.R..~~T\nT.RRR~~~T\nTR..~~~RT\nT..~~~..T\nTR~~~RR.T\nT~~~...~T\nT~~RRR~+T\nTTTTTTTTT\n",(9, 9), (1, 1), 1),
    ("mapper_tests/map_13.txt", "TTTTTTTTTTT\nT.T.~.....T\nT.~RT.T.T.T\nT~R.T...R.T\nTRT.T.T~T.T\nT~.TT~R.T.T\nTTRRT.TRT.T\nT+~TT.R~TLT\nTTTTTTTTTTT\n",(9, 11), (7, 9), 1),
    ("mapper_tests/map_14.txt", "++++++\n++++++\n++L+++\n",(3, 6), (2, 2), 17),
    ("mapper_tests/map_15.txt", "TTTTTTTTTTT\nT.........T\nT~RL......T\nTRTTT~TTT.T\nT...T+T...T\nT.R.TRT.TTT\nT.......~+T\nTTT....R..T\nTT~~...TTTT\nT+.T......T\nTTTTTTTTTTT\n",(11, 11), (2, 3), 3),
    ]

@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    map_file, stage_grid, stage_bounds, character_pos, score_req = request.param
    map = stage(map_file)
    return map, stage_grid, stage_bounds, character_pos, score_req

def test_start(map_stage):
    map, stage_grid, stage_bounds, character_pos, score_req = map_stage
    map.start()
    assert (map.y, map.x) == stage_bounds
    assert (map.character.y_coords, map.character.x_coords) == character_pos
    assert map.score_req == score_req

def test_display(map_stage):
    map, stage_grid, stage_bounds, character_pos, score_req = map_stage
    map.start()
    assert display(map, True) == stage_grid
