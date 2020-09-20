import json
import data


# puts data from data.py to data.json
def py_to_json():
    lst = []
    with open('data.json', 'w') as f:
        lst.append(data.goals)
        lst.append(data.teachers)
        json.dump(lst, f)


# adds goal to teachers with given ids
def add_goal_to_teachers(ids, goal):
    with open('data.json') as f:
        teachers = json.load(f)
    for teacher in teachers[1]:
        if int(teacher['id']) in ids:
            teachers[1][teacher['id']]['goals'].append(goal)
    with open('data.json', 'w') as f:
        json.dump(teachers, f)


# clears json files for further uses (for booking.json and request.json)
def clear_json(name):
    empty = []
    with open(name, 'w') as f:
        json.dump(empty, f)


if __name__ == "__main__":
    pass


