import json
import data


def py_to_json():
    lst = []
    with open('data.json', 'w') as f:
        lst.append(data.goals)
        lst.append(data.teachers)
        json.dump(lst, f)


def add_goal_to_teachers(ids, goal):
    with open('data.json') as f:
        teachers = json.load(f)[1]
    for teacher in teachers:
        if teacher['id'] in ids:
            teachers[teacher['id']]['goals'].append(goal)
    with open('data.json', 'w') as f:
        json.dump(teachers, f)


def main():
    add_goal_to_teachers()


if __name__ == "__main__":
    main()


