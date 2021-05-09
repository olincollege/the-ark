"""
Test the ArkController Class
"""
import pytest
from the_ark_game import LevelOneArkGame
from the_ark_controller import ArkController

test_model = LevelOneArkGame()
test_seeds = test_model.generate_seeds()
test_obstacles = test_model.generate_obstacles()
test_controller = ArkController(test_model,
                                test_obstacles,
                                test_seeds)

initial_player_cases = [
    # Check that the player is on the right level.
    (test_controller.game, test_model),
    # Check that the player's surface width is correct
    (test_controller.surf.get_width(), 61),
    # Check that the player's surface  height is correct
    (test_controller.surf.get_height(), 61),
    # Check that player spawns in the correct x position
    (test_controller.rect.centerx, 100),
    # Check that player spawns in the correct y position
    (test_controller.rect.centery, test_controller.game.SCREEN_HEIGHT-61),
]

# Test if player has the correct initial values.
@pytest.mark.parametrize("attribute,value", initial_player_cases)
def test_player_initial_attributes(attribute, value):
    """
    Check that the player's initial values are the ones intended.
    Args:
        attribute: The attribute that the code generates for the player.
        value: The value that each attribute should be.
    """
    assert attribute == value
