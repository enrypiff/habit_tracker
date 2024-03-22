import pytest
from db import get_db, add_habit, increment_traking, get_tracking, get_habits
from tracker import Tracker
from habit import Habit
from analytics import get_current_streak, get_longest_streak
import os

class TestDB:
    def setup_method(self):
        self.db = get_db('test.db')
        add_habit(self.db, 'test', 'test', 'daily', '2021-01-01 00:00:00')
        increment_traking(self.db, 'test', '2021-01-01 00:00:00')
        increment_traking(self.db, 'test', '2021-01-02 00:00:00')
        increment_traking(self.db, 'test', '2021-01-03 00:00:00')

    def test_traker(self):
        tracker = Tracker()
        tracker.update_habits(self.db)
        assert len(tracker.habits) == 1
        assert tracker.habits[0].name == 'test'
        assert tracker.habits[0].description == 'test'
        assert tracker.habits[0].periodicity == 'daily'
        assert tracker.habits[0].created == '2021-01-01 00:00:00'

        tracker.create_habit(self.db, 'test2', 'test2', 'daily', '2021-01-01 00:00:00')
        tracker[-1].add_completed(self.db, '2021-01-01 00:00:00')
        tracker[-1].add_completed(self.db, '2021-01-02 00:00:00')
        tracker[-1].add_completed(self.db, '2021-01-03 00:00:00')

        assert get_current_streak(tracker.habits[0]) == 3
        assert get_longest_streak(tracker.habits[0]) == 3

    def teardown_method(self):
        self.db.close()
        os.remove('test.db')
