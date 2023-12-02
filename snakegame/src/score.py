class Score:
    def __init__(self, score):
        self.score = score

    def increase(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def show(self):
        return self.score
