import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_color(conn, color):
    sql = ''' INSERT INTO colors(color) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, color)
    return cur.lastrowid

def select_all_colors(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM colors")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"vuellet.db"

    sql_create_colors_table = """ CREATE TABLE IF NOT EXISTS colors (
                                      id integer PRIMARY KEY,
                                      color text NOT NULL
                                  );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_colors_table)
        ## create a new project
        # color = ('[color, text, array]')
        # project_id = create_project(conn, color)
        # print("=> Query all colors")
        # select_all_colors(conn)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
