import pytest
from mapper import stage
from player import character

MAP_ATTRIBUTES = [("default.txt", (7, 6), 2)]

@pytest.fixture(params=MAP_ATTRIBUTES)
def map_stage(request):
    map_file, character_pos, score_req = request.param
    map = stage(map_file)
    return map, character_pos, score_req

def player(char: character):
    attributes = getattr(char)
    return


def test_start(map_stage):
    map, character_pos, score_req = map_stage
    map.start()
    # assert map.object_list == map_grid
    assert map.character == character((character_pos), (map.y, map.x), None, map)
    assert map.score_req == score_req

