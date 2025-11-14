import pytest
from mapper import stage
from player import character

MAP_ATTRIBUTES = [("default.txt", (6,8), 2)]

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
    print((map.character.x_coords, map.character.y_coords),( map.character.x_bound, map.character.y_bound), map.character.curr_tile, map.character.curr_stage)
    print(character_pos,( map.x, map.y), None, map)
    print(map == map.character.curr_stage)
    # assert map.object_list == map_grid
    #assert map.character == character((character_pos), (map.x, map.y), None, map)
    assert (map.character.x_coords, map.character.y_coords) == character_pos
    assert (map.character.x_bound, map.character.y_bound) == (map.x, map.y)
    assert map.character.curr_tile == None
    assert map.character.curr_stage == map
    assert map.score_req == score_req
    print("skib")

