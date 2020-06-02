import sqlite3
from sqlite3 import Error

class DataBase:
    def __init__(self):
        self.db_file = r"vuellet.db"
        self.conn = None
        self.create_connection()
        self.init_table()


    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except Error as e:
            print(e)

        return self.conn

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_color(self, colors):
        sql = ''' INSERT INTO colors(color) VALUES(?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (colors,))
        self.conn.commit()
        return cur.lastrowid

    def select_all_colors(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM colors")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def init_table(self):
        sql_create_colors_table = """ 
            CREATE TABLE IF NOT EXISTS colors (
                id integer PRIMARY KEY,
                color text NOT NULL
            );"""
        if self.conn is not None:
            self.create_table(self.conn, sql_create_colors_table)
        else:
            print("Error! cannot create the database connection.")

