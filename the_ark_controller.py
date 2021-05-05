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
    
    def __init__(self, ark_game, blocks):
        """
        Creates a new ArkController instance.
        """
        super().__init__() 
        self._image = pygame.image.load("cute_cat.png")
        self._surf = pygame.Surface((61, 61))
        self._rect = self.surf.get_rect(center = (300, 300))
        self._game = ark_game;
        self._walls = blocks
        
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
    
    @property
    def pos(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._pos
    
    @property
    def vel(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._vel
    
    @property
    def walls(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._walls

    def wall_collisions(self):
        """Handle collisions with walls."""
        self.rect.centerx = self.pos.x
        for wall in pygame.sprite.spritecollide(self, self.walls, False):
            if self.vel.x > 0:
                self.rect.right = wall.rect.left
            elif self.vel.x < 0:
                self.rect.left = wall.rect.right
            self.pos.x = self.rect.centerx

        self.rect.centery = self.pos.y
        for wall in pygame.sprite.spritecollide(self, self.walls, False):
            if self.vel.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.vel.y < 0:
                self.rect.top = wall.rect.bottom
            self.pos.y = self.rect.centery       
    
    def move(self, game):
        """
        Makes the player's avatar move left from the
        player's POV.
        """
        if pygame.sprite.spritecollideany(self, self.walls):
            pressed_keys = pygame.key.get_pressed()
            if (self.rect.top > 1 and self.rect.top != wall.rect.bottom):
                if pressed_keys[K_UP]:
                     self.rect.move_ip(0, -5)
            if (self.rect.bottom < game.SCREEN_HEIGHT - 1 and 
            self.rect.bottom != wall.rect.top):
                if pressed_keys[K_DOWN]:
                     self.rect.move_ip(0,5)

            if (self.rect.left > 1 and
            self.rect.left != wall.rect.right):
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if (self.rect.right < game.SCREEN_WIDTH and
            self.rect.right != wall.rect.left):     
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)
    
    
