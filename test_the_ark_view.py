"""
Test the ArkView Class
"""
import pytest
import pygame as pg
from the_ark_game import LevelOneArkGame
from the_ark_view import ArkView

test_model = LevelOneArkGame()
test_view = ArkView(test_model)
display_surf = test_view.set_screen()

screen_cases = [
    # Check if the screen window has been initialized.
    ((pg.display.get_init()), (True)),
    # Check if the screen window is of the correct size.
    (pg.display.get_window_size(), (test_model.SCREEN_WIDTH,
                                    test_model.SCREEN_HEIGHT)),
    # Check if the screen window has the correct caption.
    (pg.display.get_caption(), ("The Ark", "The Ark")),
    # Check that only one display is initialized.
    ((pg.display.get_num_displays()), (1)),
]

# Test the set_screen function
@pytest.mark.parametrize("actual,expected", screen_cases)
def test_set_screen(actual,expected):
    """
    Check that screen window is initialized with the correct properties
    
    Args:
        actual: The actual value of specific screen window property.
        expected: The intended vaue of that property.
    """
    assert actual == expected