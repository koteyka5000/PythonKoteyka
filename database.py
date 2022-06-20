import sqlite3

def read_from_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user (name text, email text)')
    users = list(c.execute('SELECT * FROM user'))
    conn.close()
    return users

def add_user(user):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO user VALUES ('{user}', '{user}@{user}.com')")
    conn.commit()
    conn.close()
