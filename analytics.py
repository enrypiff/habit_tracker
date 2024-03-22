from datetime import datetime, timedelta

def get_current_streak(self):
    count = 0
    if self.periodicity == "daily":
        return get_current_streak_day(self)
    elif self.periodicity == "weekly":
        return get_current_streak_week(self)

def get_current_streak_day(self):
    count = 0
    self.completed.sort(reverse=True)
    for c in self.completed:
        last = datetime.strptime(c[0], "%Y-%m-%d %H:%M:%S.%f")
        difference = datetime.now().date() - last.date()
        if difference == timedelta(days=count):
            count += 1
        elif difference < timedelta(days=count):
            pass
        else:
            break
    return count

def get_current_streak_week(self):
    count = 0
    self.completed.sort(reverse=True)
    tmp = datetime.now().date()
    for c in self.completed:
        last = datetime.strptime(c[0], "%Y-%m-%d %H:%M:%S.%f")
        difference = tmp - last.date()
        if (difference >= timedelta(weeks=0)) and (difference < timedelta(weeks=1)):
            count += 1
            tmp = last.date() - timedelta(last.date().weekday()+1)
        elif difference < timedelta(weeks=0):
            pass
        else:
            break
    return count


def get_longest_streak(self):
    if self.periodicity == "daily":
        return get_longest_streak_day(self)
    elif self.periodicity == "weekly":
        return get_longest_streak_week(self)

def get_longest_streak_day(self):
    count, longest = 0, 0
    self.completed.sort(reverse=True)
    most_recent = datetime.now().date()
    for c in self.completed:
        last = datetime.strptime(c[0], "%Y-%m-%d %H:%M:%S.%f")
        difference = most_recent - last.date()
        if difference == timedelta(days=count):
            count += 1
        elif difference < timedelta(days=count):
            pass
        else:
            most_recent = last.date()
            count = 1
        if count > longest:
            longest = count
    return longest

def get_longest_streak_week(self):
    count, longest = 0, 0
    self.completed.sort(reverse=True)
    tmp = datetime.now().date()
    for c in self.completed:
        last = datetime.strptime(c[0], "%Y-%m-%d %H:%M:%S.%f")
        difference = tmp - last.date()
        if (difference >= timedelta(weeks=0)) and (difference < timedelta(weeks=1)):
            count += 1
            tmp = last.date() - timedelta(last.date().weekday() + 1)
        elif difference < timedelta(weeks=0):
            pass
        else:
            tmp = last.date() - timedelta(last.date().weekday() + 1)
            count = 1
        if count > longest:
            longest = count
    return longest
