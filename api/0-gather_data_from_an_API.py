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
    title = ""

    for name in data_user:
        if int(argv[1]) == name.get("id"):
            data_name = name.get("name")
            print(data_name)

    for data in data_todos:
        count_true = 0
        total_count = 0

        if int(argv[1]) == data.get("userId"):
            if data.get("completed") is True:
                count_true += 1
            print(count_true)
        
        if int(argv[1]) == data.get("completed"):
            if data("completed") is True and data("completed") is False:
                total_count += 1
                print(total_count)
        
        if argv[1] == data.get("title"):
            title = data.get("title")
            print(title)

        print("Employee {} is done with tasks({}/{})"
              .format(data_name, count_true, total_count))
        print("     {}".format(title))