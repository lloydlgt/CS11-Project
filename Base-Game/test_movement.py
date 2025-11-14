import pytest
from mapper import stage
from player import input_handler

MAP_ATTRIBUTES = [
    ("default.txt", "dddddddddddddddddddddddssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaa", (7, 9), None, "~"), 
    ("map.txt", "WtWAwfwdadwh9dawd9w9a62y2h2h2h2", (2,7), None, "."), 
    ("mapper_tests/map_1.txt", "Saaddddyst", (6, 5), "*", "."),
    ("mapper_tests/map_2.txt", "aasdwsdadappp!Awaw", (0, 0), None, "."),
    ("mapper_tests/map_3.txt", "Ddawwed", (2, 1), None, "."),
    ("mapper_tests/map_4.txt", "Wddw", (3, 1), None, "."),
    ("mapper_tests/map_5.txt", "Wd", (2, 2), None, "."),
    ("mapper_tests/map_6.txt", "A", (29, 0), None, "."),
    ("mapper_tests/map_7.txt", "Ssdd", (3, 3), None, "."),
    ("mapper_tests/map_8.txt", "Ass", (1, 1), None, "~"),
    ("mapper_tests/map_9.txt", "Taassdddd", (4, 4), None, "."),
    ("mapper_tests/map_10.txt", "Add", (4, 2), None, "."),
    ("mapper_tests/map_11.txt", "WawawWAWADQDDDD", (2, 3), None, "."),
    ("mapper_tests/map_12.txt", "Wawawawawawaswswsw", (1, 1), None, "."),
    ("mapper_tests/map_13.txt", "WwwwwWwwwaAssss", (7, 4), None, "~"),
    ("mapper_tests/map_14.txt", "WwwwWww", (2, 0), None, "."),
    ("mapper_tests/map_15.txt", "dds", (5, 3), None, "~"),
    ]

@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    map_file, movement_string, current_character_location, curr_tile, tile_floor = request.param
    map = stage(map_file)
    return map, movement_string, current_character_location, curr_tile, tile_floor


def test_start(map_stage):
    map, movement_string, current_character_location, curr_tile, tile_floor = map_stage
    map.start()
    input_handler(movement_string, map)
    tile = map.object_list[current_character_location[1]][current_character_location[0]] 
    assert (map.character.x_coords, map.character.y_coords) == current_character_location
    assert map.character.curr_tile == curr_tile
    assert tile.tile_floor == tile_floor

