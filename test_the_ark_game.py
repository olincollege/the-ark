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

initial_game_cases = [
    # Check that black color constant is the correct value
    (test_model.BLACK, (0, 0, 0)),
    # Check that white color constant is the corrcet value
    (test_model.WHITE, (255, 255, 255)),
    # Check that the width of the screen is 682 pixels, the correct size
    (test_model.SCREEN_WIDTH, 682),
    # Check that the height of the screen is 512 pixels, the correct size
    (test_model.SCREEN_HEIGHT, 512),
    # Check that the level the game iniitializes on is the first level
    (test_model.level, 1),
    # Check that the number of lives the player starts with is three
    (test_model.lives, 3),
    # Check that the initial score of the player is zero
    (test_model.score, 0),
]

lose_life_cases = [
    # Check that a player with three lives loses one life and now has two
    ((3, 1), 2),
    # Check that a player with three lives loses two lives and now has one
    ((3, 2), 1),
    # Check that a player with three lives loses three lives and now has zero
    ((3, 3), 0),
    # Check that lose_life still returns 0 after the player already has zero lives
    ((3, 4), 0),
    # Check that a player with two lives loses one life and now has one
    ((2, 1), 1),
    # Check that a player with two lives loses two lives and now has zero
    ((2, 2), 0),
    # Check that lose_life still returns 0 after the player already has zero lives
    ((2, 3), 0),
    # Check that a player with one life loses one life and now has zero
    ((1, 1), 0),
    # Check that lose_life still returns 0 after the player already has zero lives
    ((1, 2), 0),
    # Check that a player with zero lives still has zero lives
    ((0, 1), 0),
]

score_cases = [
    # Check that the score increases by 1
    ((0, 1), 1),
    ((0, 2), 2),
    ((0, 3), 3),
    ((1, 1), 2),
    ((1, 2), 3),
    (())
]

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

# Test that each attribute of the Ark Game class and its subclasses is
# correctly initialized
@pytest.mark.parametrize("attribute,value", initial_game_cases)
def test_game_initial_attributes(attribute, value):
    """
    Check that the games initial class and instance attributes are their
    intended values.
    Args:
        attribute: The attribute that the code generates for the game.
        value: The value that each attribute should be.
    """
    assert attribute == value

# Test that lose_life function works correctly
@pytest.mark.parametrize("lives,value", lose_life_cases)
def test_lose_life(lives, value):
    """
    Check that the lives of the the player decrease by one if they have
    more than zero lives and that if they have zero lives, that number
    remains zero.
    Args:
        attribute: The number of lives the player has before they lose
                    a life.
        value: The number of lives the player has after they lose a life..
    """
    test_model.set_lives(lives[0])
    i = 0
    while i < lives[1]:
        new_num_lives = test_model.lose_life()
        i += 1

    assert new_num_lives == value

# Test that each comet obstacle of the first level only spawns in the correct
# x-coordinate range.
@pytest.mark.parametrize("attribute,value", comet_xposition_cases)
def test_generate_obstacles_xpositions(attribute, value):
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
def test_generate_obstacles_ypositions(attribute, value):
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
def test_generate_seeds(attribute, value):
    """
    Check that the carrot icons spawn in the right position in the right
    order.
    Args:
        attribute: The position that the code generates for the icon.
        value: The position each icon should be spawned at.
    """
    assert attribute == value
