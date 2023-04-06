#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress .
"""


import requests
from sys import argv
import json


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_user = user.json()
    data_todos = todos.json()
    data_username = ""
    Po = []
    d2 = {}
    r2 = {}

    for name in data_user:
        if int(argv[1]) == name.get("id"):
            userId = name.get("id")
            data_username = name.get("username")
    
    with open('USER_ID.json', 'w') as file:
        for data in data_todos:
            
            if int(argv[1]) == data.get("userId"):
                r2["task"] = data.get("title")
                r2["completed"] = data.get("completed")
                r2["username"] = data_username
                Po.append(r2)

        d2[userId] = Po
        print(d2)
        c3 = json.dumps(d2)
        file.write(c3)