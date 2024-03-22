from habit import Habit
from tracker import Tracker
from db import get_db
from analytics import (get_list_tracked_habits, get_list_habits_same_periodicity,
                       get_longest_streak_habits, get_longest_streak_habit,
                       get_current_streak, get_longest_streak)
from datetime import datetime, timedelta
import questionary
import os

tracker = Tracker()
def cli():

    user_choices = ["Main", "Test", "New", "Exit"]
    exit = False


    main_choice = questionary.select(
        "What DB do you want to use?", choices=user_choices).ask()

    db_name = 'main.db'

    if main_choice == user_choices[0]:
        db_name = 'main.db'
    elif main_choice == user_choices[1]:
        db_name = 'test.db'
    elif main_choice == user_choices[2]:
        db_name = questionary.text("What is the name of the new DB?").ask()
    elif main_choice == user_choices[3]:
        exit = True

    db = get_db(db_name)

    tracker.update_habits(db)

    choices = ["Create a new habit", "Add completed event", "Analyse", "Exit"]
    periodicity_choices = ["daily", "weekly"]

    while not exit:
        os.system('cls')
        home_choice = questionary.select(
            "What do you want to do?", choices=choices).ask()
        if home_choice == choices[0]:
            name = questionary.text("What is the name of the habit?").ask()
            description = questionary.text("What is the description of the habit?").ask()
            periodicity = questionary.select("What is the periodicity of the habit?",
                                             choices=periodicity_choices).ask()
            created = tracker.create_habit(db, name, description, periodicity, datetime.now())
            if created:
                print(f"Habit {name} created")
            else:
                print(f"Habit {name} already exists")
            print("\n")
        elif home_choice == choices[1]:
            try:
                habit_selected = questionary.select("Which habit do you want to update?",
                                           choices=[habit.name for habit in tracker.habits]).ask()

                day_choice = [str(datetime.now().today().date()-timedelta(days=i)) for i in range(7)]
                for habit in tracker.habits:
                    if habit.name == habit_selected:
                        day_selected = questionary.select("On which day? (YYYY-MM-DD)", choices=day_choice).ask()
                        added = habit.add_completed(db, day_selected)
                        if added:
                            print(f"Habit {habit_selected} updated")
                        else:
                            print(f"Habit {habit_selected} not updated")
            except:
                print("No habits defined")

            questionary.press_any_key_to_continue().ask()

        elif home_choice == choices[2]:

            tracker.update_completed(db)

            analyse_choices = ["Basic analysis - list of all habits",
                               "Basic analysis - list of habits with the same periodicity",
                               "Basic analysis - list of longest run streak of all habits",
                               "Basic analysis - list of longest run streak of a given habit",
                               "Info of all currently tracked habits",
                               "Info of all habits with the same periodicity",
                               "Info of a given habit",
                               "Info of the longest run streak of all habits"]
            analyse_choice = questionary.select("What do you want to analyse?", analyse_choices).ask()

            if analyse_choice == analyse_choices[0]:
                print("List of all tracked habits")
                for h in get_list_tracked_habits(tracker):
                    print("Habit name: ", h)

            elif analyse_choice == analyse_choices[1]:
                periodicity = questionary.select("Which periodicity do you want to analyse?",
                                                choices=periodicity_choices).ask()
                print(f"List of habits with periodicity {periodicity}")
                for h in get_list_habits_same_periodicity(tracker, periodicity):
                    print("Habit name: ", h)

            elif analyse_choice == analyse_choices[2]:
                print("List of longest run streak of all habits")
                print(f"Longest run streak: {get_longest_streak_habits(tracker)}")

            elif analyse_choice == analyse_choices[3]:
                try:
                    habit_name = questionary.select("Which habit do you want to analyse?",
                                                   choices=[habit.name for habit in tracker.habits]).ask()
                    print(f"Longest run streak for habit {habit_name}")
                    print(f"Longest run streak: {get_longest_streak_habit(tracker, habit_name)}")
                except:
                    print("No habits defined")

            elif analyse_choice == analyse_choices[4]:
                for habit in tracker.habits:
                    print(f"Habit name: {habit.name}")
                    print(f"Periodicity: {habit.periodicity}")
                    print(f"Current streak: {get_current_streak(habit)}")
                    print(f"Longest streak: {get_longest_streak(habit)}")
                    print("_"*30)

            elif analyse_choice == analyse_choices[5]:
                periodicity = questionary.select("Which periodicity do you want to analyse?",
                                                choices=periodicity_choices).ask()
                for habit in tracker.habits:
                    if habit.periodicity == periodicity:
                        print(f"Habit name: {habit.name}")
                        print(f"Periodicity: {habit.periodicity}")
                        print(f"Current streak: {get_current_streak(habit)}")
                        print(f"Longest streak: {get_longest_streak(habit)}")
                        print("_"*30)

            elif analyse_choice == analyse_choices[6]:
                try:
                    habit_name = questionary.select("Which habit do you want to analyse?",
                                                   choices=[habit.name for habit in tracker.habits]).ask()
                    for habit in tracker.habits:
                        if habit.name == habit_name:
                            print(f"Habit name: {habit.name}")
                            print(f"Periodicity: {habit.periodicity}")
                            print(f"Current streak: {get_current_streak(habit)}")
                            print(f"Longest streak: {get_longest_streak(habit)}")
                            print("_" * 30)
                except:
                    print("No habits defined")

            elif analyse_choice == analyse_choices[7]:
                longest = 0
                for habit in tracker.habits:
                    tmp_longest = get_longest_streak(habit)
                    if tmp_longest > longest:
                        longest = tmp_longest
                        habit_name = habit.name
                if longest > 0:
                    print(f"The longest run streak is {longest} for habit {habit_name}")
                else:
                    print("No habits have been completed")
                print("_" * 30)
            questionary.press_any_key_to_continue().ask()

        elif home_choice == choices[3]:
            db.close()
            exit = True
        else:
            print("Invalid choice")
            db.close()


if __name__ == "__main__":
    cli()