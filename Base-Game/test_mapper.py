import pytest
from mapper import stage
from player import character

MAP_ATTRIBUTES = [
    ("default.txt", (11, 12), (8, 6), 2), 
    ("map.txt", (13, 9), (8, 2), 1), 
    ("mapper_tests/map_1.txt", (9, 9), (4, 4), 1),
    ("mapper_tests/map_2.txt", (3, 3), (2, 2), 8),
    ("mapper_tests/map_3.txt", (5, 5), (3, 1), 1),
    ("mapper_tests/map_4.txt", (5, 5), (3, 1), 1),
    ("mapper_tests/map_5.txt", (5, 7), (3, 1), 1),
    ("mapper_tests/map_6.txt", (30, 30), (0, 29), 21),
    ("mapper_tests/map_7.txt", (7, 5), (1, 1), 1),
    ("mapper_tests/map_8.txt", (7, 8), (1, 2), 1),
    ("mapper_tests/map_9.txt", (9, 9), (4, 4), 4),
    ("mapper_tests/map_10.txt", (6, 7), (2, 5), 0),
    ("mapper_tests/map_11.txt", (9, 9), (3, 1), 1),
    ("mapper_tests/map_12.txt", (9, 9), (1, 1), 1),
    ("mapper_tests/map_13.txt", (9, 11), (7, 9), 1),
    ("mapper_tests/map_14.txt", (3, 6), (2, 2), 17),
    ("mapper_tests/map_15.txt", (11, 11), (2, 3), 3),
    ]

@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    map_file, stage_bounds, character_pos, score_req = request.param
    map = stage(map_file)
    return map, stage_bounds, character_pos, score_req

def test_start(map_stage):
    map, stage_bounds, character_pos, score_req = map_stage
    map.start()
    assert (map.y, map.x) == stage_bounds
    assert (map.character.y_coords, map.character.x_coords) == character_pos
    assert map.score_req == score_req


