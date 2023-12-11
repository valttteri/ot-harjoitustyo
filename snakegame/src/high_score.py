class HighScore:
    """
    A class for creating high score objects
    """

    def __init__(self, score: int, timestamp):
        """
        Constructor for the class

        Args:
            score: the score that player wanted to save
            timestamp: the moment when this object was created
        """
        self.score = score
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.score} - {self.timestamp}"
