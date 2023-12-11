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
        self.score = score

    def increase(self):
        """
        Increase score by one
        """
        self.score += 1

    def reset(self):
        """
        Set score back to zero
        """
        self.score = 0

    def show(self):
        """
        Returns the current score
        """
        return self.score
