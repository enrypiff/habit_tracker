# Habit tracker app

This is a habit tracker app that allows you to track your habits. 
You can add and delete habits. You can also mark habits as done for the day.

To interreact with the app, you will use the command line interface.
The app will prompt you with options to choose from to make the experience enjoyable.

Before running the app, you need to install the dependencies.

To install the dependencies, run the following command in the terminal:

```bash
pip install -r requirements.txt
```

To test the app, run the following command in the terminal:

```bash
pytest .
```

This will run the tests and show you the results.


Then, to run the app, run the following command in the terminal:

```bash
python main.py
```

The app will start and you can start tracking your habits.


When the app starts running, you will see the following options:

![image](https://github.com/enrypiff/habit_tracker/assets/139701172/c2f41fe1-2834-4b1e-9b3f-52157ab82ad6)


If you select test, the app will use the test_data.db containing some predefined habits with completed days.
If you select main instead you can use a new database to add your own habits.

After that you can choose what you want to do on the following menù

![image](https://github.com/enrypiff/habit_tracker/assets/139701172/6914e251-73bf-4cd7-9a91-8fcc2e78daee)

For example create a new habit to track:

![image](https://github.com/enrypiff/habit_tracker/assets/139701172/700d5147-b258-4d74-9df3-8b70023935d3)

Delete one:

![image](https://github.com/enrypiff/habit_tracker/assets/139701172/bc226f58-67c2-4d0b-8983-1ce7546252a5)

Mark an habit activity as done for a specific day (up to the previous seven days):

![image](https://github.com/enrypiff/habit_tracker/assets/139701172/e4b68832-9ac7-494d-b1cf-02b52e489ffe)

Or just analyse the habits alredy registered:

![image](https://github.com/enrypiff/habit_tracker/assets/139701172/ca8e56c0-a20b-4e1e-90ad-3e8f94e84f4c)

After a selection the app will go back on the main menù so that you can continue withou restarting the app.


Enjoy!
