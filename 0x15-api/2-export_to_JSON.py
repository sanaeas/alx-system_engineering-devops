#!/usr/bin/python3
"""Exports tasks owned by an employee to a JSON file"""
import json
import requests
import sys


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    employee = requests.get(f'https://jsonplaceholder.typicode.com/\
users/{emp_id}')
    todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={emp_id}')

    todos_list = todos.json()
    username = employee.json().get('username')
    filename = f'{emp_id}.json'

    data = {str(emp_id): [{"task": task["title"],
                           "completed": task["completed"],
                           "username": username} for task in todos_list]}

    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(data, file)
