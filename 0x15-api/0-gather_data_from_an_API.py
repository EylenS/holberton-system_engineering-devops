#!/usr/bin/python3
'''This script uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    URL_name = 'https://jsonplaceholder.typicode.com/users/'
    URL_todos = 'https://jsonplaceholder.typicode.com/todos?userId='
    dictUser = requests.get(URL_name + user_id).json()
    employeeName = dictUser.get('name')
    dictTodos = requests.get(URL_todos + user_id).json()
    totalTasks = len(dictTodos)
    doneTasks = []
    for i in dictTodos:
        if i.get('completed') is True:
            doneTasks.append(i.get('title'))
            nDoneTasks = len(doneTasks)
    print('Employee {} is done with tasks({}/{}):'.
          format(employeeName, nDoneTasks, totalTasks))
    for task in doneTasks:
        print('\t{}'.format(task))
