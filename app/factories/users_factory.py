
import json


def create_users(chemin):
    users = json.load(chemin)

    for u in users:
        print(f"  {u.login} -> {u.age}")

