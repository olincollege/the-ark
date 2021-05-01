import pygame, sys
from pygame.locals import *
import random, time


class ArkView():
    """
    A class that represents the game view of the game,
    The Ark.
    """
    pygame.init()
    
    def __init__(self, ark_game):
        """
        Creates a new ArkController instance.
        """
        self._game = ark_game
        
    @property
    def game(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._game
    
    def draw(self):
        """
        Creates the game map that players will see when they play.
        """
        # We will use Pygame to populate this method
        pass
    

    
    
    
    
        