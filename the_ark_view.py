"""
The View class for The Ark.
"""
import pygame

#Setting up Fonts


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
        self._font = pygame.font.SysFont("Verdana", 60)
        self._font_small = pygame.font.SysFont("Verdana", 20)
    @property
    def game(self):
        """
        Return the value of the private attribute, self._game.
        """
        return self._game
    @property
    def font(self):
        """
        Return the value of the private attribute, self._font.
        """
        return self._font
    @property
    def font_small(self):
        """
        Return the value of the private attribute, self._font_small.
        """
        return self._font_small
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
        display_surf = pygame.display.set_mode((self.game.SCREEN_WIDTH, 
                                               self.game.SCREEN_HEIGHT))
        display_surf.fill(self.game.WHITE)
        pygame.display.set_caption("The Ark")
        return display_surf
    def update_screen(self, display_surf, all_sprites, movable_sprites):
        """
        Updates and redraws all sprites and text on the screen.
        Args:
            display_surf: The window screen surface of the game
            all_sprites: The Sprite Group that holds all of the sprites
            movable_sprites: The Sprite Group that holds all of the
            sprites that have move methods.
        Returns:
            This method does not return anything.
        """
        # updates the window screen and the Score and Lives text
        display_surf.blit(self.game.background, (0,0))
        scores = self.font_small.render(f"SCORE: {self.game.score}", True, self.game.WHITE)
        display_surf.blit(scores, (self.game.SCREEN_WIDTH-100,10))
        life = self.font_small.render(f"LIVES: {self.game.lives}", True, self.game.WHITE)
        display_surf.blit(life, (self.game.SCREEN_WIDTH-100,30))
        # updates the sprites
        for sprite in all_sprites:
            display_surf.blit(sprite.image, sprite.rect)
            if sprite in movable_sprites:
                sprite.move()  
    def game_won(self, display_surf):
        """
        Updates screen background and tells player that they have
        won the game.
        Args:
            display_surf: The window screen surface of the game.
        Returns:
            This method does not return anything.
        """
        game_won = self._font.render("You won!", True, self.game.WHITE)
        img = pygame.image.load("win.jpg")
        display_surf.blit(img, (0,0))
        display_surf.blit(game_won, (self.game.SCREEN_WIDTH/2,
                                     self.game.SCREEN_HEIGHT/2))
        pygame.display.update()
    def game_lost(self, display_surf):
        """
        Updates screen background and tells player that they have
        lost the game.
        Args:
            display_surf: The window screen surface of the game.
        Returns:
            This method does not return anything.
        """
        game_over = self._font.render("Game Over", True, self.game.WHITE)
        img = pygame.image.load("lose.jpg")
        display_surf.blit(img, (0,0))
        display_surf.blit(game_over, (self.game.SCREEN_WIDTH/2,
                                      self.game.SCREEN_HEIGHT/2))
        pygame.display.update()
        