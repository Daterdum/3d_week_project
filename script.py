import json
import data


def py_to_json():
    lst = []
    with open('data.json', 'w') as f:
        lst.append(data.goals)
        lst.append(data.teachers)
        json.dump(lst, f)


