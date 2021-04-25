# Another possible implementatation is to have a single
# move method that takes a direction as input

class ArkController():
    """
    A class that represents the player/controller of the game,
    The Ark.
    """
    
    left = "keyboard input from <- arrow key"
    right = "keyboard input from -> arrow key"
    up = "keyboard input from up arrow key"
    down = "keyboard input from down arrow key"
    
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

           
    def move_left(self):
        """
        Makes the player's avatar move left from the
        player's POV.
        """
        pass
    
    def move_right(self):
        """
        Makes the player's avatar move right from the
        player's POV.
        """
        pass
    

    def move_up(self):
        """
        Makes the player's avatar move up from the
        player's POV.
        """
        pass
    

    def move_down(self):
        """
        Makes the player's avatar move down from the
        player's POV.
        """
        pass
