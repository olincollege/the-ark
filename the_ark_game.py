"""
The Model class for The Ark.
"""
import random
import pygame


class ArkGame():
    """
    A class that represents the state of the game,
    The Ark.
    """
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SCREEN_WIDTH = 682
    SCREEN_HEIGHT = 512
    SPEED = 5
    background = pygame.image.load("volcano.jpeg")
    def __init__(self):
        self._level = 1
        self._lives = 3
        self._score = 0
    @property
    def lives(self):
        """
        Return the value of the private attribute, self._lives.
        """
        return self._lives
    @property
    def score(self):
        """
        Return the value of the private attribute, self._score.
        """
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
    
class LevelOneArkGame(ArkGame):
    """
    A class that represents the state of the first level of the
    game, The Ark.
    """
    background = pygame.image.load("volcano.jpeg")
    def __init__(self):
        """
        Creates a Level Two game model.
        """
        super().__init__()  
    def generate_seeds(self):
        """
        Creates the seed icons for the level, which are carrots.
        Args:
            This method has no arguments.
        Returns:
            A list of the carrot icons to be spawned in Level One.
        """
        seed_img = "carrot.png"
        seeds = pygame.sprite.Group(Seed(seed_img, 200, 400),
                                    Seed(seed_img, 500, 250),
                                    Seed(seed_img, 250, 100))
        return seeds

    def generate_obstacles(self):
        """
        Creates the obstacles for the level, which are three comets.
        The speeds of the comets are 3, 4, and 5 pixels/frame, respectively.
        Args:
            This method has no arguments.
        Returns:
            A list of comets to be spawned in Level One.
        """
        comets = pygame.sprite.Group(Comet(self,2), Comet(self,3), Comet(self,4))  
        return comets
class LevelTwoArkGame():
    """
    A class that represents the state of the second level of the
    game, The Ark.
    """
    background = pygame.image.load("wasteland.jpg")
    def __init__(self):
        """
        Creates a Level Two game model.
        """
        super().__init__()    
class Comet(pygame.sprite.Sprite):
    """
    A class that represents the falling comets, which are
    the obstacles of Level One of The Ark.
    """
    def __init__(self, game, speed):
        """
        Creates a new Comet sprite.
        """
        super().__init__()
        self._game = game
        self._image = pygame.image.load("comet.png")
        self._surf = pygame.Surface((42,31))
        self._rect = self.surf.get_rect(center = \
                                  (random.randint(40,self.game.SCREEN_WIDTH-40),0))
        self._speed = speed
    def move(self):
        """
        Makes the Comet fall at a certain speed and respawn
        at a new, random x-position at the top of the screen.
        """
        self.rect.move_ip(0,self.speed)
        if self.rect.top > self._game.SCREEN_HEIGHT:
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
    """
    A class that represents the seed icons that are the goals
    for each level.
    """
    def __init__(self, img, xpos, ypos):
        """
        Creates a new Comet sprite.
        """
        super().__init__()
        self._image = pygame.image.load(img)
        self._surf = pygame.Surface((61, 61))
        self._rect = self.surf.get_rect(center = (xpos, ypos))
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
    