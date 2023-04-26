#!/usr/bin/python3
"""returns information about empl0yee todo list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        u.get("name"), len(completed), len(todo)))
    [print("\t {}".format(c)) for m in completed]

