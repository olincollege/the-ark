import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

class ArkController(pygame.sprite.Sprite):
    """
    A class that represents the player/controller of the game,
    The Ark.
    """
    
    def __init__(self, ark_game):
        """
        Creates a new ArkController instance.
        """
        super().__init__() 
        self._image = pygame.image.load("cute_cat.png")
        self._surf = pygame.Surface((50, 100))
        self._rect = self.surf.get_rect(center = (150, 500))
        self._game = ark_game;
        
    @property
    def image(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._image
    
    @property
    def surf(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._surf
    
    @property
    def rect(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._rect
    
    @property
    def game(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._game

           
    def move(self):
        """
        Makes the player's avatar move left from the
        player's POV.
        """
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
             self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
             self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:    # < SCREEN_WIDTH     
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    
