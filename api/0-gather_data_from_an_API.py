#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    EMPLOYEE_NAME = user.json()[0]["name"]
    NUMBER_OF_DONE_TASKS = todos.json()[0]["completed"]
    TOTAL_NUMBER_OF_TASKS = todos.json()[0]["completed"]
    TASK_TITLE = todos.json()[0]["title"]

    print("Employee {} is done with tasks({}/{})"
          .format(EMPLOYEE_NAME,
                  NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    print("     {}".format(TASK_TITLE))
