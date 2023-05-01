#!/usr/bin/python3
"""returns information about empl0yee todo list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    Id = argv[1]

    employees = requests.get("{}/users/{}".format(url, Id)).json()
    todos = requests.get(url + "/todos", params={"userId": Id}).json()

    completed_tasks = []
    for data in todos:
        if data.get('completed') is True:
            completed_tasks.append(data.get('title'))

    employee_name = employees.get('name')
    total_num_of_tasks = len(todos)
    num_of_tasks_done = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          num_of_tasks_done, total_num_of_tasks))

    for title in completed_tasks:
        print("\t {}".format(title))

