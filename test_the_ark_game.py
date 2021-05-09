"""
Test the ArkGame, Comet, and Seed Classes.
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

comet_xposition_cases = [
    # Check that the first comet spawns in the correct x position range
    (test_obstacles.sprites()[0].rect.centerx, (40, test_model.SCREEN_WIDTH-40)),
    # Check that the second comet spawns in the correct x position range
    (test_obstacles.sprites()[1].rect.centerx, (40, test_model.SCREEN_WIDTH-40)),
    # Check that the third comet spawns in the correct x position range
    (test_obstacles.sprites()[2].rect.centerx, (40, test_model.SCREEN_WIDTH-40)),
]

comet_yposition_cases = [
    # Check that the first comet spawns in the correct y position
    (test_obstacles.sprites()[0].rect.centery, 0),
    # Check that the second comet spawns in the correct x position
    (test_obstacles.sprites()[1].rect.centery, 0),
    # Check that the third comet spawns in the correct x position
    (test_obstacles.sprites()[2].rect.centery, 0),
]

seeds_cases = [
    # Check that the first carrot icon spawns at the correct x position.
    (test_seeds.sprites()[0].rect.centerx, 200),
    # Check that the first carrot icon spawns at the correct y position.
    (test_seeds.sprites()[0].rect.centery, 400),
    # Check that the second carrot icon spawns at the correct x position.
    (test_seeds.sprites()[1].rect.centerx, 500),
    # Check that the second carrot icon spawns at the correct y position.
    (test_seeds.sprites()[1].rect.centery, 250),
    # Check that the third carrot icon spawns at the correct x position.
    (test_seeds.sprites()[2].rect.centerx, 250),
    # Check that the third carrot icon spawns at the correct y position.
    (test_seeds.sprites()[2].rect.centery, 100),
]

# Test that each comet obstacle of the first level only spawns in the correct
# x-coordinate range.
@pytest.mark.parametrize("attribute,value", comet_xposition_cases)
def test_comet_xpositions(attribute, value):
    """
    Check that the comet obstacles only spawn between the 40th pixel and the
    pixel 40 pixels left of the widthe of the screen (both included).
    Args:
        attribute: The x-position that the code generates for the comet.
        value: The x-position each icon should be spawned at.
    """
    pos = (attribute >= value[0]) and (attribute <= value[1])
    assert pos

# Test that each comet obstacle of the first level spawns at the top of the screen
@pytest.mark.parametrize("attribute,value", comet_yposition_cases)
def test_comet_ypositions(attribute, value):
    """
    Check that the comet obstacles spawn at the top of the screen, at
    pixel 0 in the y direction.
    Args:
        attribute: The y-position that the code generates for the comet.
        value: The y-position each icon should be spawned at.
    """
    assert attribute == value

# Test that each seed icon of the first level spawns at the right position.
@pytest.mark.parametrize("attribute,value", seeds_cases)
def test_seed_positions(attribute, value):
    """
    Check that the carrot icons spawn in the right position in the right
    order.
    Args:
        attribute: The position that the code generates for the icon.
        value: The position each icon should be spawned at.
    """
    assert attribute == value
