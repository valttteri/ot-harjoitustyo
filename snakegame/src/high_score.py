from datetime import datetime


class HighScore:
    def __init__(self, score: int, timestamp):
        #!TODO self.nickname = nickname
        self.score = score
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.score} - {self.timestamp}"


if __name__ == "__main__":
    h = HighScore(20, datetime.now().strftime("%d.%m.%Y klo %H:%M"))
    print(h.timestamp)
