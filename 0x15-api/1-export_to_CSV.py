#!/usr/bin/python3
"""Exports data inCSV format."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    Id = argv[1]

    employees = requests.get("{}/users/{}".format(url, Id)).json()
    todos = requests.get(url + "/todos", params={"userId": Id}).json()

    userName = employees.get('username')
    fileName = Id + ".csv"

    line = []
    for info in todos:
        line.append([Id, userName, info.get('completed'),
                    info.get('title')])

    with open(fileName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for r in line:
            writer.writerow(r)

