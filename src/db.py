import sqlite3
import datetime

def get_db(name='main.db'):
    """
    Create a connection to the database
    :param name: name of the database
    :return: return the connection
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db

def create_tables(db):
    """
    Create the tables in the database if they do not exist
    :param db: db connection
    :return: none
    """
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habits ( name TEXT PRIMARY KEY, description TEXT, periodicity TEXT, created TIMESTAMP, UNIQUE(name))
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS records ( habit_name TEXT, date TIMESTAMP, 
    FOREIGN KEY (habit_name) REFERENCES habit(name), UNIQUE(date, habit_name))""")

    db.commit()

def add_habit(db, name, description, periodicity, created=datetime.datetime.now()):
    """
    Add a habit to the database
    :param db: db connection
    :param name: name of the habit
    :param description: description of the habit
    :param periodicity: periodicity of the habit (daily, weekly)
    :param created: date and time when the habit was created (default is now)
    :return: none
    """
    cur = db.cursor()
    cur.execute("INSERT OR IGNORE INTO habits VALUES(?, ?, ?, ?)", (name, description, periodicity, created))
    db.commit()

def delete_habit(db, name):
    """
    Delete a habit from the database
    :param db: db connection
    :param name: name of the habit
    :return: none
    """
    cur = db.cursor()
    cur.execute("DELETE FROM habits WHERE name = ?", (name,))
    db.commit()

    cur.execute("DELETE FROM records WHERE habit_name = ?", (name,))
    db.commit()

def add_event(db, name, event_date=None):
    """
    Add an event to the tracker
    :param db: db connection
    :param name: name of the habit
    :param event_date: date of the event
    :return: none
    """
    cur = db.cursor()
    if not event_date:
        event_date = datetime.datetime.now().date()
    if type(event_date) is str:
        event_date = datetime.datetime.strptime(event_date, "%Y-%m-%d").date()

    cur.execute("INSERT OR IGNORE INTO records VALUES (?, ?)", (name, event_date))
    db.commit()

def get_records(db, name):
    """
    Get all records for a given habit
    :param db: db connection
    :param name: name of the habit
    :return: list of dates
    """
    cur = db.cursor()
    cur.row_factory = lambda cursor, row: row[0] # return only the date instead of a tuple
    cur.execute("SELECT date FROM records WHERE habit_name = ?", (name,))
    db.commit()
    return cur.fetchall()

def get_habits(db):
    """
    Get all habits from the database
    :param db: db connection
    :return: list of habits (name, description, periodicity, created)
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habits")
    db.commit()
    return cur.fetchall()