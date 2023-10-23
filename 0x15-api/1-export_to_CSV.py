#!/usr/bin/python3
"""Exports tasks owned by an employee to a CSV file"""
import csv
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
    filename = f'{emp_id}.csv'

    with open(filename, 'w', encoding='UTF8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_list:
            writer.writerow([emp_id, username, task['completed'],
                             task['title']])
