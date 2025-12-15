import pytest
from mapper import stage

# ("Path of map file", (x, y), "tile_object", "tile_floor")

MAP_ATTRIBUTES = [
    ("default.txt", (6, 1), "+", "."),
    ("map.txt", (3, 3), None, "."),
    ("mapper_tests/map_1.txt", (1, 1), None, "."),
    ("mapper_tests/map_2.txt", (2, 2), "L", "."),
    ("mapper_tests/map_3.txt", (2, 3), None, "."),
    ("mapper_tests/map_4.txt", (2, 1), None, "~"),
    ("mapper_tests/map_5.txt", (3, 2), "R", "."),
    ("mapper_tests/map_6.txt", (0, 29), "+", "."),
    ("mapper_tests/map_7.txt", (2, 4), None, "~"),
    ("mapper_tests/map_8.txt", (4, 4), None, "~"),
    ("mapper_tests/map_9.txt", (4, 6), None, "~"),
    ("mapper_tests/map_10.txt", (1, 4), "x", "."),
    ("mapper_tests/map_11.txt", (8, 0), "T", "."),
    ("mapper_tests/map_12.txt", (0, 0), "T", "."),
    ("mapper_tests/map_13.txt", (9, 7), "L", "."),
    ("mapper_tests/map_14.txt", (0, 0), "+", "."),
    ("mapper_tests/map_15.txt", (2, 2), "R", "."),
    ("default.txt", (6, 4), "T", "."),
    ("map.txt", (6, 5), "*", "."),
    ("mapper_tests/map_1.txt", (8, 8), "T", "."),
    ("mapper_tests/map_2.txt", (0, 1), "+", "."),
    ("mapper_tests/map_3.txt", (0, 0), "T", "."),
    ("mapper_tests/map_4.txt", (1, 3), "L", "."),
    ("mapper_tests/map_5.txt", (3, 4), "T", "."),
    ("mapper_tests/map_6.txt", (23, 12), None, "."),
    ("mapper_tests/map_7.txt", (3, 2), None, "."),
    ("mapper_tests/map_8.txt", (6, 1), None, "~"),
    ("mapper_tests/map_9.txt", (6, 3), "R", "."),
    ("mapper_tests/map_10.txt", (4, 4), "*", "."),
    ("mapper_tests/map_11.txt", (2, 7), None, "~"),
    ("mapper_tests/map_12.txt", (1, 4), None, "."),
    ("mapper_tests/map_13.txt", (4, 1), None, "~"),
    ("mapper_tests/map_14.txt", (2, 2), "L", "."),
    ("mapper_tests/map_15.txt", (1, 9), "+", "."),
]


@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    """Create an instance of the stage and return references of each stage attribute

    :param request: Map from list of maps
    :type request: _type_
    :return: Each of the stage's attributes
    :rtype: _type_
    """
    map_file, tile_coordinates, tile_object, tile_floor = request.param
    map = stage(map_file)
    return map, tile_coordinates, tile_object, tile_floor


def test_start(map_stage):
    """Validates the tile at the given coordinates on the stage

    :param map_stage: _description_
    :type map_stage: _type_
    """
    map, tile_coordinates, tile_object, tile_floor = map_stage
    map.start()
    tile_being_checked = map.object_list[tile_coordinates[1]][tile_coordinates[0]]
    assert tile_being_checked.tile_object == tile_object
    assert tile_being_checked.tile_floor == tile_floor
