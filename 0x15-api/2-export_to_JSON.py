#!/usr/bin/python3
'''This script uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import json
import requests
from sys import argv


if __name__ == '__main__':
    u_id = argv[1]
    URL_name = 'https://jsonplaceholder.typicode.com/users/'
    URL_todos = 'https://jsonplaceholder.typicode.com/todos?userId='

    # Info about employee according to the id passed
    dictUser = requests.get(URL_name + u_id).json()
    username = dictUser.get('username')

    # List of dicts, info about tasks: userId, title, completed
    dictTodos = requests.get(URL_todos + u_id).json()
    # print(dictTodos)
    # print('-----')

    taskList = []
    listOfDict = []
    for task in dictTodos:
        if task['userId'] == int(u_id):
            taskList.append(task)
    # print(taskList)
    # print('---')

    for task in taskList:
        listOfDict.append({'task': task['title'],
                           'completed': task['completed'],
                           'username': username})
    # print(listOfDict)

    dict = {u_id: listOfDict}
    with open('{}.json'.format(u_id), mode='w') as jsonFile:
        json.dump(dict, jsonFile)
