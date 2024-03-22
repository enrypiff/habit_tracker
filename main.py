from habit import Habit
from tracker import Tracker
from db import get_db
from analytics import get_current_streak, get_longest_streak
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



    while not exit:
        os.system('cls')
        home_choice = questionary.select(
            "What do you want to do?", choices=choices).ask()
        if home_choice == choices[0]:
            name = questionary.text("What is the name of the habit?").ask()
            description = questionary.text("What is the description of the habit?").ask()
            periodicity = questionary.select("What is the periodicity of the habit?",
                                             choices=["daily", "weekly"]).ask()
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
                for habit in tracker.habits:
                    if habit.name == habit_selected:
                        added = habit.add_completed(db)
                        if added:
                            print(f"Habit {habit_selected} updated")
                        else:
                            print(f"Habit {habit_selected} not updated")
            except:
                print("No habits defined")
            questionary.press_any_key_to_continue().ask()

        elif home_choice == choices[2]:
            analyse_choices = ["All currently tracked habits",
                               "Habits with the same periodicity",
                               "Longest run streak of all defined habits",
                               "Longest run streak for a given habit",
                               "Longest run streak"]
            analyse_choice = questionary.select("What do you want to analyse?", analyse_choices).ask()

            for habit in tracker.habits:
                habit.get_completed(db)

            if analyse_choice == analyse_choices[0]:
                for habit in tracker.habits:
                    print(f"Habit name: {habit.name}")
                    print(f"Periodicity: {habit.periodicity}")
                    print(f"Current streak: {get_current_streak(habit)}")
                    print("_"*30)
            elif analyse_choice == analyse_choices[1]:
                periodicity = questionary.select("Which periodicity do you want to analyse?",
                                                choices=["daily", "weekly"]).ask()
                for habit in tracker.habits:
                    if habit.periodicity == periodicity:
                        print(f"Habit name: {habit.name}")
                        print(f"Periodicity: {habit.periodicity}")
                        print(f"Current streak: {get_current_streak(habit)}")
                        print("_"*30)
            elif analyse_choice == analyse_choices[2]:
                for habit in tracker.habits:
                    print(f"Habit name: {habit.name}")
                    print(f"Periodicity: {habit.periodicity}")
                    print(f"Longest streak: {get_longest_streak(habit)}")
                    print("_"*30)
            elif analyse_choice == analyse_choices[3]:
                habit_name = questionary.select("Which habit do you want to analyse?",
                                               choices=[habit.name for habit in tracker.habits]).ask()
                for habit in tracker.habits:
                    if habit.name == habit_name:
                        print(f"Current streak: {get_current_streak(habit)}")
                        print(f"Longest streak: {get_longest_streak(habit)}")
                        print("_" * 30)
            elif analyse_choice == analyse_choices[4]:
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

    # habit_list = Habit("run", "111", "daily")
    # habit_list.create_habit(db)
    # habit_list.add_completed(db)
    # tmp_time = datetime.now() - timedelta(days=1)
    # habit_list.add_completed(db, tmp_time)
    #
    # tmp_time = tmp_time - timedelta(days=1)
    # habit_list.add_completed(db, tmp_time)
    #
    # tmp_time = tmp_time - timedelta(days=1)
    # habit_list.add_completed(db, tmp_time)
    #
    # print(habit_list.get_completed(db))
    # print(habit_list.get_last(db))


if __name__ == "__main__":
    cli()