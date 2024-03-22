from habit import Habit
from db import get_habits

from datetime import datetime
class Tracker:
    """
    Class to represent a tracker
    """
    habits = []
    def __init__(self):
        """
        Initialize the tracker
        """
        pass

    def update_habits(self, db):
        """
        Populate the habits from the database
        :param db: db connection
        :return: none
        """
        raw_habit_list = get_habits(db)
        for habit in raw_habit_list:
            self.habits.append(Habit(habit[0], habit[1], habit[2], datetime.strptime(habit[3], "%Y-%m-%d %H:%M:%S.%f")))

    def create_habit(self, db, name, description, periodicity, created=datetime.now()):
        """
        Create a habit in the tracker and if not present write it in the database
        :param db: db connection
        :param name: name of the habit
        :param description: description of the habit
        :param periodicity: periodicity of the habit (daily, weekly)
        :param created: date and time when the habit was created
        :return: True if the habit was created and added to the database, False if the habit already exists
        """
        present = False
        for i in range(len(self.habits)):
            if name == self.habits[i].name:
                present = True
                break
        if not present:
            self.habits.append(Habit(name, description, periodicity, created))
            self.habits[-1].create_habit(db)
            return True
        else:
            return False

    def delete_habit(self, db, name):
        """
        Delete a habit from the tracker and the database
        :param db: db connection
        :param name: name of the habit
        :return: none
        """
        for i in range(len(self.habits)):
            if name == self.habits[i].name:
                self.habits[i].delete_habit(db)
                del self.habits[i]
                break

    def update_completed(self, db):
        """
        Populate the completed events for all habits from the database
        :param db: db connection
        :return: none
        """
        for habit in self.habits:
            habit.get_completed(db)
