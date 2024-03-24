# Habit tracker app

This is a simple habit tracker app that allows you to track your habits. 
You can add and delete habits. You can also mark habits as done for the day.

To interreact with the app, you will use the command line interface.
The app will prompt you with options to choose from to make the experience enjoyable.

Before running the app, you need to install the dependencies.

To install the dependencies, run the following command in the terminal:

```bash
pip install -r requirements.txt
```

Then, to run the app, run the following command in the terminal:

```bash
python main.py
```

The app will start and you can start tracking your habits.

To test the app, run the following command in the terminal:

```bash
python pytest .
```

This will run the tests and show you the results.

When the app starts running, you will see the following options:

If you select test, the app will use the test_data.db containing some predefined habits with completed days.
If you select main instead you can use a new database to add your own habits.


Enjoy!
