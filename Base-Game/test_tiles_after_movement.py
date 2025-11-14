import pytest
from mapper import stage
from player import input_handler

MAP_ATTRIBUTES = [
    ("default.txt", "aaaaa", (2, 8), "R", "."), 
    ("map.txt", "wwwwp!dd!s!wwwp", (2,5), None, "."), 
    ("mapper_tests/map_1.txt", "w", (4, 2), None, "_"),
    ("mapper_tests/map_2.txt", "wwaasd", (1, 1), "L", "."),
    ("mapper_tests/map_3.txt", "WWwaaddsw!ssss", (0, 0), "T", "."),
    ("mapper_tests/map_4.txt", "wdds", (3, 3), None, "~"),
    ("mapper_tests/map_5.txt", "wddd", (5, 2), "R", "."),
    ("mapper_tests/map_6.txt", "asdawdasdaw!dwadsdwdwwdw!sdaWADWAS!dddpppwwwfl!!F", (6, 7), None, "."),
    ("mapper_tests/map_7.txt", "dssssss", (2, 4), None, "_"),
    ("mapper_tests/map_8.txt", "swdddsdsssaaaawawddd", (3, 3), None, "_"),
    ("mapper_tests/map_9.txt", "awaawa", (2, 5), "R", "."),
    ("mapper_tests/map_10.txt", "assdddp", (5, 4), None, "."),
    ("mapper_tests/map_11.txt", "wwwwadwwaadLMAOssssaassddwwwwwsddwwaaaaaassaassdssa", (3, 5), "R", "."),
    ("mapper_tests/map_12.txt", "dddswaasdwdsswaaasddwdssssddwsaawddwdss!dddswaasdwd", (3, 5), None, "~"),
    ("mapper_tests/map_13.txt", "WwwwwWwwwaAssss", (7, 4), None, "~"),
    ("mapper_tests/map_14.txt", "aaaawwwdddddsssaaa!", (2, 1), "+", "."),
    ("mapper_tests/map_15.txt", "dds", (5, 3), None, "~"),
    ]

@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    map_file, movement_string, tile_to_check_coords, tile_object, tile_floor = request.param
    map = stage(map_file)
    return map, movement_string, tile_to_check_coords, tile_object, tile_floor


def test_start(map_stage):
    map, movement_string, tile_to_check_coords, tile_object, tile_floor = map_stage
    map.start()
    input_handler(movement_string, map)
    tile = map.object_list[tile_to_check_coords[1]][tile_to_check_coords[0]] 
    assert tile.tile_object == tile_object
    assert tile.tile_floor == tile_floor
