#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""


import requests
from sys import argv
import csv


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_user = user.json()
    data_todos = todos.json()
    data_username = ""

    for name in data_user:
        if int(argv[1]) == name.get("id"):
            data_username = name.get("username")

    with open('USER_ID.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
        for data in data_todos:
            li = []
            if int(argv[1]) == data.get("userId"):
                li.append(data.get("userId"))
                li.append(data_username)
                li.append(data.get("completed"))
                li.append(data.get("title"))
                writer.writerow([li])
    file.close()
