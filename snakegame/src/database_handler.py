import datetime
import sqlite3


class Database:
    def __init__(self, location:str):
        """
        Luo SQLite-tietokannan huipputulosten tallentamista varten ja hallinnoi sitä.

        Attributes
        ----------
        location : str
            Minne tallennetaan.
        """

        self.location = location

    def initialize_database(self):
        pass

    def clear_database(self):
        pass
    
    def get_high_scores(self):
        pass

    def update_high_scores(self):
        pass