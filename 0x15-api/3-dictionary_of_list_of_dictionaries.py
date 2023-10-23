#!/usr/bin/python3
"""Exports tasks of all employees to a JSON file"""
import json
import requests


if __name__ == '__main__':
    employees = (requests.get('https://jsonplaceholder.typicode.com/users')
                         .json())
    all_tasks = {}

    for emp in employees:
        emp_id = emp['id']
        todos = requests.get(f'https://jsonplaceholder.typicode.com/\
todos?userId={emp_id}').json()
        username = emp['username']
        task_data = [{'username': username, 'task': task['title'],
                      'completed': task['completed']} for task in todos]
        all_tasks[str(emp_id)] = task_data

    filename = 'todo_all_employees.json'

    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(all_tasks, file)
