import sqlite3
import datetime

def get_db(name='main.db'):
    db = sqlite3.connect(name)
    create_tables(db)
    return db

def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habit ( name TEXT PRIMARY KEY, description TEXT, periodicity TEXT, created TIMESTAMP, UNIQUE(name))
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker ( habit_name TEXT, date TIMESTAMP, 
    FOREIGN KEY (habit_name) REFERENCES habit(name), UNIQUE(date, habit_name))""")

    db.commit()

def add_habit(db, name, description, periodicity, created):
    cur = db.cursor()
    cur.execute("INSERT OR IGNORE INTO habit VALUES(?, ?, ?, ?)", (name, description, periodicity, created))
    db.commit()

def increment_traking(db, name, event_date=None):
    cur = db.cursor()
    if not event_date:
        event_date = datetime.datetime.now()
    cur.execute("INSERT OR IGNORE INTO tracker VALUES (?, ?)", (event_date, name))
    db.commit()

def get_tracking(db, name):
    cur = db.cursor()
    cur.execute("SELECT date FROM tracker WHERE habit_name=?", (name,))
    db.commit()
    return cur.fetchall()

def get_habits(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM habit")
    db.commit()
    return cur.fetchall()