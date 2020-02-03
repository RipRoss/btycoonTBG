import json
import os


def load_config(filepath):
    with open(filepath, "r") as cfile:
        data = json.load(cfile)

    return data

print(os.getcwd())

db_config = load_config('data_access/config/settings.json')
