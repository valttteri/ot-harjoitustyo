import sqlite3
from high_score import HighScore


class Database:
    def __init__(self, location: str):
        """
        Luo SQLite-tietokannan huipputulosten tallentamista varten ja hallinnoi sitä.

        Attributes
        ----------
        location : str
            Minne tallennetaan.
        """

        self.location = location
        self.initialize_database()

    def initialize_database(self):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            score INTEGER,
            time TIMESTAMP
            )
        """
        )

        connection.commit()
        connection.close()

    def clear_database(self):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS scores")

        connection.commit()
        connection.close()

    def add_high_score(self, high_score):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO scores (score, time)
            VALUES (?, ?)""",
            (high_score.score, high_score.timestamp),
        )

        connection.commit()
        connection.close()

    def get_high_scores(self):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute("SELECT score, time from scores")
        sql_scores = cursor.fetchall()

        score_list = []

        for sql_score in sql_scores:
            score_list.append(HighScore(sql_score[0], sql_score[1]))

        connection.commit()
        connection.close()

        if len(score_list) >= 10:
            return score_list[:10]

        return score_list

    def update_database(self, high_scores: list):
        connection = sqlite3.connect(self.location)
        self.clear_database()
        self.initialize_database()

        for high_score in high_scores:
            self.add_high_score(high_score)

        connection.commit()
        connection.close()
