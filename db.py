
import sqlite3
db_file = 'dbscript.db'

class DataBase:

    def __init__(self, connect):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()


    async def set_sale(self, sale):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET sale=(?)""",
                                       [sale])

    async def set_amount(self, amount):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET amount=(?)""",
                                       [amount])

    async def get_sale(self):
        with self.connect:
            return self.cursor.execute("""SELECT sale FROM users""").fetchone()

    async def get_amount(self):
        with self.connect:
            return self.cursor.execute("""SELECT amount FROM users""").fetchone()