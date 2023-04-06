#!/usr/bin/python3
"""
    script to export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_user = user.json()
    data_todos = todos.json()

    d2 = {}

    
    for name in data_user:
            userId = name.get("id")
            data_username = name.get("username")   
            Po = []
            for data in data_todos:
                if data.get("userId") == userId:
                    r2 = {}
                    r2["username"] = data_username
                    r2["task"] = data.get("title")
                    r2["completed"] = data.get("completed")
                    Po.append(r2)
            d2[userId] = Po
            print(d2)

    c3 = json.dumps(d2)
    with open('todo_all_employees.json', 'w') as file:
        file.write(c3)
