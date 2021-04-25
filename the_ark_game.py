
class ArkGame():
    """
    A class that represents the state of the game,
    The Ark.
    """
    def __init__(self):
        self._level = 1
        self._lives = 3
    
    @property
    def level(self):
        return self._level
    
    @property
    def lives(self):
        return self._lives
    

    def lose_life()
        """
        Decreases the number of lives the player's
        avater has.
        
        Returns:
            Returns the number of lives the player has left.
            If the player has 1 life left, then they lose that life
            and -1 is returned.
        """
        if lives > 1:
            return self._lives = self._lives - 1
        else:
            return -1
        
        
    def next_level:
        """
            Moves the player to the next level of the game
            and redraws the map (view) of the game.
        """
        pass
    
    
    