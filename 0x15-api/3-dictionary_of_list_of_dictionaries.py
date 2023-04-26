#!/usr/bin/python3
"""Exports data in JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for r in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for s in users}, jsonfile)
