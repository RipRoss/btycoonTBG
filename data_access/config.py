import json


def load_config(filepath):
    with open(filepath, "r") as cfile:
        data = json.loads(cfile)

    return data


db_config = load_config('config/settings.json')
