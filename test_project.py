from datetime import datetime, timedelta
from src import Tracker, db, analytics

import os

class TestDB:
    def setup_method(self):
        """
        Setup the test database
        :return: none
        """
        self.db_conn = db.get_db('test.db')

        # create a habit direct in the database
        db.add_habit(self.db_conn, 'run', 'run 30 min', 'daily')
        db.add_event(self.db_conn, 'run', datetime.now().date())
        db.add_event(self.db_conn, 'run', datetime.now().date() - timedelta(days=1))
        db.add_event(self.db_conn, 'run', datetime.now().date() - timedelta(days=2))

        db.add_habit(self.db_conn, 'swim', 'swim 1h', 'weekly')
        db.add_event(self.db_conn, 'swim', '2024-03-01')
        db.add_event(self.db_conn, 'swim', '2024-03-02')
        db.add_event(self.db_conn, 'swim', '2024-03-06')

    def test_traker(self):
        """
        Test the tracker class and its methods
        :return: none
        """
        tracker = Tracker()
        tracker.update_habits(self.db_conn)
        tracker.update_completed(self.db_conn)

        print(tracker.habits[0].completed[0])
        assert len(tracker.habits) == 2
        assert tracker.habits[0].name == 'run'
        assert tracker.habits[0].description == 'run 30 min'
        assert tracker.habits[0].periodicity == 'daily'
        assert tracker.habits[0].created.date() == datetime.now().date()

        assert analytics.get_current_streak(tracker.habits[0]) == 3
        assert analytics.get_longest_streak(tracker.habits[0]) == 3

        assert tracker.habits[1].name == 'swim'
        assert tracker.habits[1].description == 'swim 1h'
        assert tracker.habits[1].periodicity == 'weekly'
        assert tracker.habits[1].created.date() == datetime.now().date()

        assert analytics.get_current_streak(tracker.habits[1]) == 0
        assert analytics.get_longest_streak(tracker.habits[1]) == 2


        tracker.create_habit(self.db_conn, 'code', 'code 1h', 'daily')
        tracker.habits[2].add_completed(self.db_conn, datetime.now().date() - timedelta(days=0))
        tracker.habits[2].add_completed(self.db_conn, datetime.now().date() - timedelta(days=1))

        tracker.habits[2].add_completed(self.db_conn, datetime.now().date() - timedelta(days=3))
        tracker.habits[2].add_completed(self.db_conn, datetime.now().date() - timedelta(days=4))
        tracker.habits[2].add_completed(self.db_conn, datetime.now().date() - timedelta(days=5))

        assert analytics.get_current_streak(tracker.habits[2]) == 2
        assert analytics.get_longest_streak_habit(tracker, 'code') == 3

        assert analytics.get_list_tracked_habits(tracker) == ['run', 'swim', 'code']
        assert analytics.get_list_habits_same_periodicity(tracker, 'daily') == ['run', 'code']
        assert analytics.get_list_habits_same_periodicity(tracker, 'weekly') == ['swim']

        tracker.create_habit(self.db_conn, 'clean apartment', 'clean all', 'weekly')
        tracker.habits[-1].add_completed(self.db_conn, '2024-02-13')
        tracker.habits[-1].add_completed(self.db_conn, '2024-02-20')
        tracker.habits[-1].add_completed(self.db_conn, '2024-02-29')
        tracker.habits[-1].add_completed(self.db_conn, '2024-03-06')

        assert analytics.get_current_streak(tracker.habits[-1]) == 0
        assert analytics.get_longest_streak(tracker.habits[-1]) == 4
        assert analytics.get_longest_streak_habit(tracker, 'clean apartment') == 4
        assert analytics.get_longest_streak_habits(tracker) == 4

        tracker.delete_habit(self.db_conn, 'clean apartment')
        assert len(tracker.habits) == 3

        tracker.create_habit(self.db_conn, 'take pills', 'take all pills for diet supplement', 'daily')
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=0))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=1))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=2))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=3))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=4))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=5))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=6))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=7))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=8))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=9))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=10))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=11))
        tracker.habits[-1].add_completed(self.db_conn, datetime.now().date() - timedelta(days=12))

        tracker.habits[-1].add_completed(self.db_conn, '2022-06-01')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-02')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-03')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-04')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-05')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-06')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-07')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-08')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-09')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-10')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-11')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-12')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-13')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-14')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-15')
        tracker.habits[-1].add_completed(self.db_conn, '2022-06-16')

        assert analytics.get_current_streak(tracker.habits[-1]) == 13
        assert analytics.get_longest_streak(tracker.habits[-1]) == 16
        assert analytics.get_longest_streak_habit(tracker, 'take pills') == 16

        assert len(db.get_habits(self.db_conn)) == 4
        assert len(db.get_records(self.db_conn, 'run')) == 3


    def teardown_method(self):
        """
        Tear down the test database and remove it
        :return: none
        """
        self.db_conn.close()
        os.remove('test.db')
