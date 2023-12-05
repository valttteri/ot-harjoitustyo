from datetime import datetime


class HighScore:
    def __init__(self, score:int): 
        #!TODO self.nickname = nickname
        self.score = score
        self.timestamp = datetime.now().strftime("%d.%m.%Y klo %H:%M")
    
    def __str__(self):
        return f"{self.score} - {self.timestamp}"

if __name__ == "__main__":
    h = HighScore(20)
    print(h.timestamp)