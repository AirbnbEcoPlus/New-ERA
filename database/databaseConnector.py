import sqlite3
con = sqlite3.connect('database/database.sqlite')
def database_connect():
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS commands(id int, name char(32), description longtext, return_type char(32), parameters longtext)")
    cur.execute("CREATE TABLE IF NOT EXISTS events(id int, name char(32), description longtext, event_type char(32), return_type char(32), parameters longtext)")