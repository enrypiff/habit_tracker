from datetime import datetime
from .db import add_habit, add_event, get_records, delete_habit

class Habit:
    """
    Class to represent a habit
    """
    def __init__(self, name: str, description: str, periodicity: str, created: datetime):
        """
        Initialize the habit
        :param self: self instance
        :param name: name of the habit
        :param description: description of the habit
        :param periodicity: periodicity of the habit (daily, weekly)
        :param created: date and time when the habit was created
        :return: none
        """
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created = created
        self.completed = [] # list of completed events

    def create_habit(self, db):
        """
        Create a habit in the database
        :param self: self instance
        :param db: db connection
        :return: none
        """
        add_habit(db, self.name, self.description, self.periodicity, self.created)

    def delete_habit(self, db):
        """
        Delete a habit from the database
        :param self: self instance
        :param db: db connection
        :return: none
        """
        delete_habit(db, self.name)

    def add_completed(self, db, date=datetime.now().date()):
        """
        Add a completed event to the habit and write it in the database
        :param self: self instance
        :param db: db connection
        :param date: date of the event
        :return: none
        """
        if not date:
            date = datetime.now().date()
        if type(date) is str:
            date = datetime.strptime(date, "%Y-%m-%d").date()

        add_event(db, self.name, date)
        self.completed.append(date)
        return True

    def get_completed(self, db):
        """
        Get all completed events from the database and store them in the habit instance
        :param self: self instance
        :param db: db connection
        :return: none
        """
        self.completed = [datetime.strptime(c, "%Y-%m-%d").date() for c in get_records(db, self.name)]