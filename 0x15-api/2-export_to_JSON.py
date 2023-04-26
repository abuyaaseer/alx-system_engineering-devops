#!/usr/bin/python3
"""Exports data in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(id)).json()
    username = u.get("username")
    todo = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.json".format(id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo]}, jsonfile)
