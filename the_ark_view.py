import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

    


class ArkView():
    """
    A class that represents the game view of the game,
    The Ark.
    """
    
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
    
    def set_screen(self):
        """
        Initializes the game screen and creates the screen
        window's surface.
        
        Args:
            This method has no arguments.
            
        Returns:
            The surface that represents the window screen the
            game.
        """
        DISPLAYSURF = pygame.display.set_mode((self.game.SCREEN_WIDTH, 
                                               self.game.SCREEN_HEIGHT))
        DISPLAYSURF.fill(self.game.WHITE)
        pygame.display.set_caption("Game")
        
        return DISPLAYSURF
    
    def update_screen(self, DISPLAYSURF, all_sprites, movable_sprites):
        """
        Updates and redraws all sprites and text on the screen.
        
        Args:
            DISPLAYSURF: The window screen surface of the game
            all_sprites: The Sprite Group that holds all of the sprites
            movable_sprites: The Sprite Group that holds all of the
            sprites that have move methods.
        
        Returns:
        This method does not return anything.
        """
        # updates the window screen and the Score and Lives text
        DISPLAYSURF.blit(self.game.background, (0,0))
        scores = font_small.render(f"SCORE: {self.game.score}", True, self.game.WHITE)
        DISPLAYSURF.blit(scores, (self.game.SCREEN_WIDTH-100,10)) 
        life = font_small.render(f"LIVES: {self.game.lives}", True, self.game.WHITE)
        DISPLAYSURF.blit(life, (self.game.SCREEN_WIDTH-100,30))
        
        # updates the sprites 
        for sprite in all_sprites:
            DISPLAYSURF.blit(sprite.image, sprite.rect)
            if sprite in movable_sprites:
                sprite.move()
    
    
    
        