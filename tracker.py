from habit import Habit
from db import get_db, get_habits

from datetime import datetime, timedelta
class Tracker:

    habits = []
    def __init__(self):
        pass

    def update_habits(self, db):
        raw_habit_list = get_habits(db)
        for habit in raw_habit_list:
            self.habits.append(Habit(habit[0], habit[1], habit[2], habit[3]))

    def create_habit(self, db, name, description, periodicity, created=datetime.now()):
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