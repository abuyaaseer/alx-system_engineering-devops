#!/usr/bin/python3
"""Exports data in JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    Id = argv[1]

    employees = requests.get("{}/users/{}".format(url, Id)).json()
    todos = requests.get(url + "/todos", params={"userId": Id}).json()

    userName = employees.get('username')
    fileName = Id + ".json"

    line = []
    for info in todos:
        info.append({'task': info.get('title'),  })
