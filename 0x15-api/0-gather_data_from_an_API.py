#!/usr/bin/python3
"""Returns information about a given employee's TODO list progress"""
import requests
import sys


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    employee = requests.get(f'https://jsonplaceholder.typicode.com/\
users/{emp_id}')
    todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={emp_id}')

    done = [task for task in todos.json() if task.get('completed', False)]
    print(f'Employee {employee.json().get("name")} is done with tasks\
({len(done)}/{len(todos.json())}):')
    for task in done:
        print(f'\t {task.get("title")}')
