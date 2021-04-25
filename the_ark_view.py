from abc import ABC, abstractmethod


class ArkView(ABC):
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
    
    @abstractmethod
    def draw(self):
        """
        Creates the game map that players will see when they play.
        """
        # We will use Pygame to populate this method
        pass
    
class LevelOneArkView(ArkView):
    
    def draw(self):
        """
        Creates the game map that players will see when they play
        the first level.
        """
        pass

class LevelTwoArkView(ArkView):
    
    def draw(self):
        """
        Creates the game map that players will see when they play
        the second level.
        """
        pass
    
    
    
    
        