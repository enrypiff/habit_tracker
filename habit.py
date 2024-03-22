from datetime import datetime, timedelta
from db import add_habit, increment_traking, get_tracking

class Habit:

    def __init__(self, name: str, description: str, periodicity: str, created: datetime):
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created = created
        self.completed = []

    def create_habit(self, db):
        add_habit(db, self.name, self.description, self.periodicity, self.created)

    def add_completed(self, db, date=datetime.now()):
        increment_traking(db, self.name, date)
        self.completed.append(datetime.now())
        return True

    def get_completed(self, db):
        data = get_tracking(db, self.name)
        self.completed = data
        return self.completed