class Score:
    """
    Class for managing the player's score
    """
    def __init__(self, score):
        """
        Constructor for the class
        
        Args:
            score: the initial score
        """
        self._score = score

    def increase(self):
        """
        Increase score by one
        """
        self._score += 1

    def reset(self):
        """
        Set score back to zero
        """
        self._score = 0

    def show(self):
        """
        Returns the current score
        """
        return self._score
