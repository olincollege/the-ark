import pygame, sys
from pygame.locals import *
import random, time


class ArkGame():
    """
    A class that represents the state of the game,
    The Ark.
    """
    pygame.init()
    
    def __init__(self):
        self._level = 1
        self._lives = 3
    
    @property
    def level(self):
        return self._level
    
    @property
    def lives(self):
        return self._lives
    

    def lose_life():
        """
        Decreases the number of lives the player's
        avater has.
        
        Returns:
            Returns the number of lives the player has left.
            If the player has 1 life left, then they lose that life
            and -1 is returned.
        """
        if lives > 1:
            self.lives = self.lives - 1
            return self.lives
        else:
            return -1
        
        
    def next_level():
        """
            Moves the player to the next level of the game
            and redraws the map (view) of the game.
        """
        pass
    
class LevelOneArkGame():
    
    def draw(self):
        """
        Creates the game map that players will see when they play
        the first level.
        """
        pass

class LevelTwoArkGame():
    
    def draw(self):
        """
        Creates the game map that players will see when they play
        the second level.
        """
        pass   
    
    
    