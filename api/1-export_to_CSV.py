#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress .
"""


import requests
from sys import argv
import csv


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_user = user.json()
    data_todos = todos.json()
    data_name = ""
    data_username = ""
    Title = ""
    task_status = ""
    count_true = 0
    total_count = 0
    userId = 0

    for name in data_user:
        if int(argv[1]) == name.get("id"):
            data_name = name.get("name")
            data_username = name.get("username")

    for data in data_todos:
        if int(argv[1]) == data.get("userId"):
            userId = data.get("userId")
            if data.get("completed") is True:
                count_true += 1

            if data.get("completed") is True or data.get("completed") is False:
                task_status = data.get("completed")
                total_count += 1

    for data in data_todos:
        if int(argv[1]) == data.get("userId"):
            if data.get("completed") is True:
                Title = data.get("title")

    
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
    #file.close()
