import pygame, sys
from pygame.locals import *
from pygame.math import Vector2
import random, time

pygame.init()

class ArkController(pygame.sprite.Sprite):
    """
    A class that represents the player/controller of the game,
    The Ark.
    """
    
    def __init__(self, game, comets, seeds):
        """
        Creates a new ArkController instance.
        """
        super().__init__()
        self._game = game;
        self._image = pygame.image.load("cute_cat.png")
        self._surf = pygame.Surface((61, 61))
        self._rect = self.surf.get_rect(center = (100, self.game.SCREEN_HEIGHT-61))
        self._comets = comets
        self._seeds = seeds
        
    @property
    def game(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._game    
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
    def comets(self):
        """
        Return the value of the private attribute, self._comets.
        """
        return self._comets
    @property
    def seeds(self):
        """
        Return the value of the private attribute, self._seeds.
        """
        return self._seeds
 
    
    def move(self):
        """
        Makes the player's avatar move left from the
        player's POV.
        """
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 1:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < self.game.SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 1:
            if pressed_keys[K_LEFT]:                
                self.rect.move_ip(-5, 0)
        if self.rect.right < self.game.SCREEN_WIDTH:     
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    
