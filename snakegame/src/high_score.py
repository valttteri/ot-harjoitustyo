from datetime import datetime


class HighScore:
    def __init__(self, score:int, nickname:str): 
        self.score = score
        self.nickname = nickname
        self.timestamp = datetime.now().strftime("%d.%m.%Y klo %H:%M")
    
    def __str__(self):
        return f"{self.score} - {self.nickname} - {self.timestamp}"

if __name__ == "__main__":
    h = HighScore(20, "mikko")
    print(h.timestamp)