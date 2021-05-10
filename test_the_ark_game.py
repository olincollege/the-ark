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

set_life_cases =[
    # Check that the player's lives are set to 0 correctly
    (0, 0),
    # Check that the player's lives are set to 1 correctly
    (1, 1),
    # Check that the player's lives are set to 2 correctly
    (2, 2),
    # Check that the player's lives are set to 3 correctly
    (3, 3),
    # Check that the player's lives are set to 4 correctly
    (4, 4)

]

life_decrease_cases = [
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

set_score_cases =[
    # Check that the player's score is set to 0 correctly
    (0, 0),
    # Check that the player's score is set to 1 correctly
    (1, 1),
    # Check that the player's score is set to 2 correctly
    (2, 2),
    # Check that the player's score is set to 3 correctly
    (3, 3),
    # Check that the player's score is set to 4 correctly
    (4, 4)

]

score_increase_cases = [
    # Check that a score of 0 increases by 1 to result in a score of 1
    ((0, 1), 1),
    # Check that a score of 0 increases by 2 to result in a score of 2
    ((0, 2), 2),
    # Check that a score of 0 increases by 3 to result in a score of 3
    ((0, 3), 3),
    # Check that a score of 1 increases by 1 to result in a score of 2
    ((1, 1), 2),
    # Check that a score of 1 increases by 2 to result in a score of 3
    ((1, 2), 3),
    # Check that a score of 2 increases by 1 to result in a score of 3
    ((2, 1), 3),
    # Check that a score of 2 that is increased by 2 still results in a score of 3
    ((2, 2), 3),
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

initial_comet_cases = [
    # Check that the first comet's surface width is correct
    (test_obstacles.sprites()[0].surf.get_width(), 42),
    # Check that the first comet's surface height is correct
    (test_obstacles.sprites()[0].surf.get_height(), 31),
    # Check that the second comet's surface width is correct
    (test_obstacles.sprites()[1].surf.get_width(), 42),
    # Check that the second comet's surface height is correct
    (test_obstacles.sprites()[1].surf.get_height(), 31),
    # Check that the third comet's surface width is correct
    (test_obstacles.sprites()[2].surf.get_width(), 42),
    # Check that the third comet's surface height is correct
    (test_obstacles.sprites()[2].surf.get_height(), 31),
]

comet_fall_cases = [
    # Check that first comet moves down 2 pixels when move() called once
    ((test_obstacles.sprites()[0], 1), 2),
    # Check that first comet moves down 4 pixels when move() called twice
    ((test_obstacles.sprites()[0], 2), 4),
    # Check that first comet moves down 6 pixels when move() called thrice
    ((test_obstacles.sprites()[0], 3), 6),
    # Check that second comet moves down 3 pixels when move() called once
    ((test_obstacles.sprites()[1], 1), 3),
    # Check that second comet moves down 6 pixels when move() called twice
    ((test_obstacles.sprites()[1], 2), 6),
    # Check that second comet moves down 9 pixels when move() called thrice
    ((test_obstacles.sprites()[1], 3), 9),
    # Check that third comet moves down 4 pixels when move() called once
    ((test_obstacles.sprites()[2], 1), 4),
    # Check that third comet moves down 8 pixels when move() called twice
    ((test_obstacles.sprites()[2], 2), 8),
    # Check that third comet moves down 12 pixels when move() called thrice
    ((test_obstacles.sprites()[2], 3), 12),
] 

comet_respawn_cases = [
    # Check that first comet respawns at the top of the screen when located
    # right at the bottom of the screen
    ((test_obstacles.sprites()[0], 0), 0),
    # Check that first comet respawns at the top of the screen when located
    # one pixel past the height of the screen
    ((test_obstacles.sprites()[0], 1), 0),
    # Check that first comet respawns at the top of the screen if located
    # ten pixels past the height of the screen
    ((test_obstacles.sprites()[0], 10), 0),
    # Check that second comet respawns at the top of the screen when located
    # right at the bottom of the screen
    ((test_obstacles.sprites()[1], 0), 0),
    # Check that second comet respawns at the top of the screen when located
    # one pixel past the height of the screen
    ((test_obstacles.sprites()[1], 1), 0),
    # Check that first comet respawns at the top of the screen if located
    # ten pixels past the height of the screen
    ((test_obstacles.sprites()[1], 10), 0),
    # Check that third comet respawns at the top of the screen when located
    # right at the bottom of the screen
    ((test_obstacles.sprites()[2], 0), 0),
    # Check that third comet respawns at the top of the screen when located
    # one pixel past the hight of the screen
    ((test_obstacles.sprites()[2], 1), 0),
    # Check that first comet respawns at the top of the screen if located
    # ten pixels past the hight of the screen
    ((test_obstacles.sprites()[2], 10), 0),
]

initial_seed_cases = [
    # Check that the first seed's surface width is correct
    (test_seeds.sprites()[0].surf.get_width(), 61),
    # Check that the first seed's surface height is correct
    (test_seeds.sprites()[0].surf.get_height(), 61),
    # Check that the second seed's surface width is correct
    (test_seeds.sprites()[1].surf.get_width(), 61),
    # Check that the second seed's surface height is correct
    (test_seeds.sprites()[1].surf.get_height(), 61),
    # Check that the third seed's surface width is correct
    (test_seeds.sprites()[2].surf.get_width(), 61),
    # Check that the third seed's surface height is correct
    (test_seeds.sprites()[2].surf.get_height(), 61),
]

# Test that each attribute of the Ark Game class and its subclasses is
# correctly initialized
@pytest.mark.parametrize("attribute,value", initial_game_cases)
def test_game_initial_attributes(attribute, value):
    """
    Check, where possible, that the game's initial class and instance
    attributes are their intended values.
    Args:
        attribute: The attribute that the code generates for the game.
        value: The value that each attribute should be.
    """
    assert attribute == value

# Test that set_lives function works correctly
@pytest.mark.parametrize("num,value", set_life_cases)
def test_set_lives(num, value):
    """
    Check that lives the player has is set to the intended number
    Args:
        num: The number to which lives is set.
        value: The number that lives should be after the function
        is run.
    """
    test_model.set_lives(num)
    new_lives = test_model.lives
    assert  new_lives == value

# Test that lose_life function works correctly
@pytest.mark.parametrize("lives,value", life_decrease_cases)
def test_lose_life(lives, value):
    """
    Check that the lives of the the player decrease by one if they have
    more than zero lives and that if they have zero lives, that number
    remains zero.
    Args:
        attribute: A tuple containing the number of lives the player has
        before the function is run, and how many times to run the function,
        respectively.
        value: The number of lives the player has after they lose a life.
    """
    test_model.set_lives(lives[0])
    i = 0
    while i < lives[1]:
        new_num_lives = test_model.lose_life()
        i += 1

    assert new_num_lives == value

# Test that set_score function works correctly
@pytest.mark.parametrize("num,value", set_score_cases)
def test_set_score(num, value):
    """
    Check that score of the player is set to the intended number
    Args:
        num: The number to which the score is set.
        value: The number that the score should be after the function
        is run.
    """
    test_model.set_score(num)
    new_score = test_model.score
    assert  new_score == value

# Test that inc_score function works correctly
@pytest.mark.parametrize("scores,value", score_increase_cases)
def test_inc_score(scores, value):
    """
    Check that the score of the the player increases by one if they have
    a score less than 3 and that if they have a score of 3, that number
    remains at 3.
    Args:
        attribute: A tuple containing the score of the player before the
        function is run, and how many times to run the function, respectively.
        value: The score of the player after the function is run.
    """
    test_model.set_score(scores[0])
    i = 0
    while i < scores[1]:
        new_score = test_model.inc_score()
        i += 1

    assert new_score == value

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

# Test that each attribute of the Comet class is correctly initialized
@pytest.mark.parametrize("attribute,value", initial_comet_cases)
def test_comet_initial_attributes(attribute, value):
    """
    Check, where possible, that the attributes of the Comet class
    are their intended values.
    Args:
        attribute: The attribute that the code generates for the game.
        value: The value that each attribute should be.
    """
    assert attribute == value

# Test that the Comets are falling at the correct speeds
@pytest.mark.parametrize("comet,value", comet_fall_cases)
def test_comet_falling(comet, value):
    """
    Check, where possible, that the comets are changing positions by the
    correct amounts when the move function is called
    Args:
        comet: A tuple containing the comet and how many times the move
        function is called, respectively.
        value: The amount of pixels the comet has moved down after the
        move function has been called a number of times.
    """
    old_position = comet[0].rect.centery
    i = 0
    while i < comet[1]:
        comet[0].move()
        i += 1
    new_position = comet[0].rect.centery
    diff = new_position - old_position
    assert diff == value

# Test that the Comets are respawning correctly when move() called
@pytest.mark.parametrize("comet,value", comet_respawn_cases)
def test_comet_respawning(comet, value):
    """
    Check, that each comet respawns at the top of the screen once they
    have moved below the bottom of the screen
    Args:
        comet: A tuple containing the comet and how many pixels below the
        screen the top of the comet is before move() is called, respectively.
        value: The intended new vertical position of the comet after
        move() is called.
    """
    comet[0].rect.top = test_model.SCREEN_HEIGHT + comet[1]
    comet[0].move()
    new_position = comet[0].rect.centery
    assert new_position == value

# Test that each attribute of the Seed class is correctly initialized
@pytest.mark.parametrize("attribute,value", initial_seed_cases)
def test_seed_initial_attributes(attribute, value):
    """
    Check, where possible, that the attributes of the Seed class
    are their intended values.
    Args:
        attribute: The attribute that the code generates for the game.
        value: The value that each attribute should be.
    """
    assert attribute == value