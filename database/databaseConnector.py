import sqlite3

con = sqlite3.connect('database/database.sqlite')


def database_connect():
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS commands(id int, name char(32), description longtext, return_type char(32), args longtext)")
    cur.execute("CREATE TABLE IF NOT EXISTS events(id int, name char(32), description longtext, event_type char(32), return_type char(32), args longtext)")
    cur.execute("CREATE TABLE IF NOT EXISTS config(name char(32), value longtext)")


# options
def add_option(name, value):
    cur = con.cursor()
    cur.execute("INSERT INTO config VALUES (?, ?)", (name, value))
    con.commit()


def get_option(name):
    cur = con.cursor()
    cur.execute("SELECT value FROM config WHERE name=?", (name,))
    return cur.fetchone()[0]


def change_option(name, value):
    cur = con.cursor()
    cur.execute("UPDATE config SET value=? WHERE name=?", (value, name))
    con.commit()


# commands
def add_command(command):
    cur = con.cursor()
    cur.execute("INSERT INTO commands VALUES (?, ?, ?, ?, ?)",
                (command.id, command.name, command.description, command.return_type, command.args))
    con.commit()


def get_command(id):
    cur = con.cursor()
    cur.execute("SELECT value FROM commands WHERE id=?", (id,))
    return cur.fetchone()[0]


def delete_command(id):
    cur = con.cursor()
    cur.execute("DELETE FROM commands WHERE id=?", (id,))
    con.commit()


# events
def add_event(event):
    cur = con.cursor()
    cur.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?, ?)",
                (event.id, event.name, event.description, event.event_type, event.return_type, event.args))
    con.commit()


def delete_event(id):
    cur = con.cursor()
    cur.execute("DELETE FROM events WHERE id=?", (id,))
    con.commit()


def get_event(id):
    cur = con.cursor()
    cur.execute("SELECT value FROM events WHERE id=?", (id,))
    return cur.fetchone()[0]
