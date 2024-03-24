from datetime import datetime, timedelta

def get_list_tracked_habits(self):
    """
    Get list of all tracked habits
    :param self: instance of Tracker
    :return: list of habit names
    """
    return [habit.name for habit in self.habits]

def get_list_habits_same_periodicity(self, periodicity):
    """
    Get list of habits with same periodicity
    :param self: istance of Tracker
    :param periodicity: value of periodicity
    :return: list of habit names
    """
    return [habit.name for habit in self.habits if habit.periodicity == periodicity]

def get_longest_streak_habits(self):
    """
    Get longest streak of all habits
    :param self: istace of Tracker
    :return: value of longest streak of all habits
    """
    longest = 0
    for habit in self.habits:
        streak = get_longest_streak(habit)
        if streak > longest:
            longest = streak
    return longest

def get_longest_streak_habit(self, habit_name):
    """
    Get longest streak of a given habit
    :param self: istace of Tracker
    :param habit_name: given habit name
    :return: value of longest streak of a given habit
    """
    for habit in self.habits:
        if habit.name == habit_name:
            return get_longest_streak(habit)


def get_current_streak(self):
    """
    Get current streak of a given habit
    :param self: instance of Habit
    :return: value of current streak
    """
    count = 0
    if self.periodicity == "daily":
        return get_current_streak_day(self)
    elif self.periodicity == "weekly":
        return get_current_streak_week(self)

def get_current_streak_day(self):
    """
    Get current streak of a given habit with daily periodicity
    :param self: instance of Habit
    :return: value of current streak
    """
    count = 0
    self.completed.sort(reverse=True)
    for last in self.completed:
        difference = datetime.now().date() - last
        if difference == timedelta(days=count):
            count += 1
        elif difference < timedelta(days=count):
            pass
        else:
            break
    return count

def get_current_streak_week(self):
    """
    Get current streak of a given habit with weekly periodicity
    :param self: instance of Habit
    :return: value of current streak
    """
    count = 0
    self.completed.sort(reverse=True)
    tmp = datetime.now().date()
    for last in self.completed:
        difference = tmp - last
        if (difference >= timedelta(weeks=0)) and (difference < timedelta(weeks=1)):
            count += 1
            tmp = last - timedelta(last.weekday()+1)
        elif difference < timedelta(weeks=0):
            pass
        else:
            break
    return count

def get_longest_streak(self):
    """
    Get longest streak of a given habit
    :param self: instance of Habit
    :return: value of longest streak
    """
    if self.periodicity == "daily":
        return get_longest_streak_day(self)
    elif self.periodicity == "weekly":
        return get_longest_streak_week(self)

def get_longest_streak_day(self):
    """
    Get longest streak of a given habit with daily periodicity
    :param self: instance of Habit
    :return: value of longest streak
    """
    count, longest = 0, 0
    self.completed.sort(reverse=True)
    most_recent = datetime.now().date()
    for last in self.completed:
        difference = most_recent - last
        if difference == timedelta(days=count):
            count += 1
        elif difference < timedelta(days=count):
            pass
        else:
            most_recent = last
            count = 1
        if count > longest:
            longest = count
    return longest

def get_longest_streak_week(self):
    """
    Get longest streak of a given habit with weekly periodicity
    :param self: instance of Habit
    :return: value of longest streak
    """
    count, longest = 0, 0
    self.completed.sort(reverse=True)
    tmp = datetime.now().date()
    for last in self.completed:
        difference = tmp - last
        if (difference >= timedelta(weeks=0)) and (difference < timedelta(weeks=1)):
            count += 1
            tmp = last - timedelta(last.weekday() + 1)
        elif difference < timedelta(weeks=0):
            pass
        else:
            tmp = last - timedelta(last.weekday() + 1)
            count = 1
        if count > longest:
            longest = count
    return longest
