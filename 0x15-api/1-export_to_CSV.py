#!/usr/bin/python3
'''This script uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import csv
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

    user_data = []
    for i in dictTodos:
        if i['userId'] == int(u_id):
            user_data.append(i)

    data = []
    for j in user_data:
        data.append({'username': username, 'id': u_id,
                     'completed': j['completed'], 'title': j['title']})

    # Writing to CSV files using the DictWriter class
    fieldnames = ['id', 'username', 'completed', 'title']

    with open('{}.csv'.format(u_id), 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for x in data:
            writer.writerow(x)
