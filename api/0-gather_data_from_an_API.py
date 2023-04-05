#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests



if __name__ == "__main__":
    api_url = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    EMPLOYEE_NAME = api_url.json()[0][""]
    NUMBER_OF_DONE_TASKS = api_url.json()[0][""]
    TOTAL_NUMBER_OF_TASKS = api_url.json()[0][""]
    TASK_TITLE = api_url.json()[0][""]

    print("Employee {} is done with tasks({}/{})".format(EMPLOYEE_NAME,
                                                         NUMBER_OF_DONE_TASKS,
                                                         TOTAL_NUMBER_OF_TASKS))
    print("     {}".format(TASK_TITLE))
