# from shroom_raider import run_input
# import controls
# # import pytest
# from unittest.mock import MagicMock

# def mock_setups():
#     mock_curr_stage = MagicMock()
#     mock_character = MagicMock()

#     mock_movement = controls.movement_keybinds
#     mock_player_action = controls.player_action_keybinds
#     mock_ui = controls.ui_keybinds

#     mock_curr_stage.character = mock_character
#     mock_curr_stage.inventory = None

#     mock_tiles = MagicMock()
#     mock_curr_stage.character.curr_tile = mock_tiles

#     return mock_curr_stage, mock_movement, mock_player_action, mock_ui, mock_character, mock_tiles

# def test_movement(mock_setups):
#     mock_curr_stage, mock_movement, mock_player_action, mock_ui, mock_character, mock_tiles = mock_setups
#     run_input('w')
#     mock_character.move.assert_called_once_with('up')



# # def test_run_input():
# #     assert ...