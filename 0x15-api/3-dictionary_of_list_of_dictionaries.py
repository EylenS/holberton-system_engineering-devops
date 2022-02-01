#!/usr/bin/python3
'''This script uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import json
import requests


if __name__ == '__main__':
    URL_users = 'https://jsonplaceholder.typicode.com/users/'
    URL_todos = 'https://jsonplaceholder.typicode.com/todos/'

    dictUser = requests.get(URL_users).json()
    dictTodos = requests.get(URL_todos).json()

    dict = {}
    username = {}

    for user in dictUser:
        # storing id user into the variable
        u_id = user['id']
        # the id as a key, list as a value for the dict:
        dict[u_id] = []  # dict = {1: [], 2: [], 3: [], 4: []}
        # getting de username according to its id, and storing
        username[u_id] = user['username']  # {"1": "Bret"}

    for data in dictTodos:
        tasks = {}
        u_id = data.get('userId')
        # the key/value are added to the dict tasks
        tasks['username'] = username.get(u_id)
        tasks['task'] = data.get('title')
        tasks['completed'] = data['completed']
        # the tasks are added as a value to the corresponding id
        dict.get(u_id).append(tasks)

    with open('todo_all_employees.json', mode='w') as jsonFile:
        json.dump(dict, jsonFile)
