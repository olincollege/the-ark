import pygame, sys
from pygame.locals import *
import random, time


class ArkGame():
    """
    A class that represents the state of the game,
    The Ark.
    """
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    SCREEN_WIDTH = 813
    SCREEN_HEIGHT = 700
    SPEED = 5
    
    background = pygame.image.load("volcano.jpg")
    
    
    
    def __init__(self):
        self._level = 1
        self._lives = 3
        self._score = 0
    
    @property
    def level(self):
        return self._level
    
    @property
    def lives(self):
        return self._lives
    @property
    def score(self):
        return self._score
    

    def lose_life(self):
        """
        Decreases the number of lives the player's
        avater has.
        
        Returns:
            Returns the number of lives the player has left.
        """
 
        self._lives -= 1
        return self._lives
    
    def inc_score(self):
        """
        Increases the score of the player when a seed is collected.
        
        Returns:
            Returns the number of seeds the player has collected.
        """
 
        self._score += 1
        return self._score    
        
    def next_level(self):
        """
            Moves the player to the next level of the game
            and redraws the map (view) of the game.
        """
        pass

    
class Comet(pygame.sprite.Sprite):
    
    def __init__(self, game, speed):
        """
        Creates a new Comet sprite.
        """
        super().__init__()
        self._game = game;
        self._image = pygame.image.load("fire.png")
        self._surf = pygame.Surface((61, 61))
        self._rect = self.surf.get_rect(center = \
                                  (random.randint(40,self.game.SCREEN_WIDTH-40),0))
        self._speed = speed;
    
    def move(self):
        """
        Makes the Comet fall at a certain speed and respawn
        at a new, random x-position at the top of the screen.
        """
        self.rect.move_ip(0,self.speed)
        if (self.rect.top > self.game.SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, self.game.SCREEN_WIDTH-40), 0)
    
    @property
    def image(self):
        """
        Return the value of the private attribute, self._image.
        """
        return self._image
    @property
    def surf(self):
        """
        Return the value of the private attribute, self._surf.
        """
        return self._surf    
    @property
    def rect(self):
        """
        Return the value of the private attribute, self._rect.
        """
        return self._rect    
    @property
    def game(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._game
    @property
    def speed(self):
        """
        Return the value of the private attribute, self._speed.
        """
        return self._speed
    
class Seed(pygame.sprite.Sprite):
    
    def __init__(self, game, img):
        """
        Creates a new Comet sprite.
        """
        super().__init__()
        self._game = game;
        self._image = pygame.image.load(img)
        self._surf = pygame.Surface((61, 61))
        self._rect = self.surf.get_rect(center = \
                                  (random.randint(40,self.game.SCREEN_WIDTH-40),
                                      random.randint(40,self.game.SCREEN_WIDTH-40)))
    
    @property
    def image(self):
        """
        Return the value of the private attribute, self._image.
        """
        return self._image
    @property
    def surf(self):
        """
        Return the value of the private attribute, self._surf.
        """
        return self._surf    
    @property
    def rect(self):
        """
        Return the value of the private attribute, self._rect.
        """
        return self._rect
    @property
    def game(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._game
    
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
    
    
    