from datetime import datetime, timedelta
from db import get_db, add_habit, add_event, get_records, get_habits
from tracker import Tracker
from habit import Habit
from analytics import (get_list_tracked_habits, get_list_habits_same_periodicity,
                       get_longest_streak_habits, get_longest_streak_habit,
                       get_current_streak, get_longest_streak)
import os

class TestDB:
    def setup_method(self):
        self.db = get_db('test.db')
        add_habit(self.db, 'test', 'test', 'daily', '2021-01-01 00:00:00')
        add_event(self.db, 'test', '2021-01-01')
        add_event(self.db, 'test', '2021-01-02')
        add_event(self.db, 'test', '2021-01-03')

    def test_traker(self):
        tracker = Tracker()
        tracker.update_habits(self.db)
        assert len(tracker.habits) == 1
        assert tracker.habits[0].name == 'test'
        assert tracker.habits[0].description == 'test'
        assert tracker.habits[0].periodicity == 'daily'
        assert tracker.habits[0].created == '2021-01-01'

        tracker.create_habit(self.db, 'test2', 'test2', 'daily', '2021-01-01 00:00:00')
        tracker[-1].add_completed(self.db, '2021-01-01')
        tracker[-1].add_completed(self.db, '2021-01-02')
        tracker[-1].add_completed(self.db, '2021-01-03')
        tracker[-1].add_completed(self.db, datetime.now().date())
        tracker[-1].add_completed(self.db, datetime.now().date() - timedelta(days=1))
        assert get_current_streak(tracker.habits[-1]) == 2
        assert get_longest_streak_habit(tracker, 'test2') == 3

        assert get_list_tracked_habits(tracker) == ['test', 'test2']
        assert get_list_habits_same_periodicity(tracker, 'daily') == ['test', 'test2']

        tracker.create_habit(self.db, 'test3', 'test2', 'weekly', '2021-01-01 00:00:00')
        tracker[-1].add_completed(self.db, datetime.now().date())
        tracker[-1].add_completed(self.db, datetime.now().date()-timedelta(days=1))

        assert get_current_streak(tracker.habits[0]) == 3
        assert get_longest_streak(tracker.habits[0]) == 3

        assert get_longest_streak_habits(tracker) == 3

    def teardown_method(self):
        self.db.close()
        os.remove('test.db')
