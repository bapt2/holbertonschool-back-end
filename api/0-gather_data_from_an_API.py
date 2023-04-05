#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_user = user.json()
    data_todos = todos.json()
    data_name = ""
    count_true = 0
    total_count = 0
    Title = ""

    for name in data_user:
        if int(argv[1]) == name.get("id"):
            data_name = name.get("name")

    for data in data_todos:
        if int(argv[1]) == data.get("userId"):
            if data.get("completed") is True:
                count_true += 1

            if data.get("completed") is True or data.get("completed") is False:
                total_count += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(data_name, count_true, total_count))

    for data in data_todos:
        if int(argv[1]) == data.get("userId"):
            if data.get("completed") is True:
                Title = data.get("title")
                print("\t {}".format(Title))
