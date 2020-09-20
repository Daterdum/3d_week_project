from flask import Flask, render_template, request
import json
from random import sample

app = Flask(__name__)
days = {"mon": "Понедельник",
        "tue": "Вторник",
        "wed": "Среда",
        "thu": "Четверг",
        "fri": "Пятница",
        "sat": "Суббота",
        "sun": "Воскресенье"}


def sort_by_rating(teachers_by_goal):
    teachers = teachers_by_goal
    has_changed = True
    while has_changed:
        has_changed = False
        for i, teacher in enumerate(teachers):
            if teacher['id'] == teachers[-1]['id']:
                continue
            if teacher['rating'] < teachers[i+1]['rating']:
                temp = teacher
                teachers[i] = teachers[i+1]
                teachers[i+1] = temp
                has_changed = True
    return teachers


@app.route('/')
def index():
    ids = sample(range(11), k=6)
    with open('data.json') as f:
        temp_teachers = json.load(f)[1]
        teachers = [x for x in temp_teachers if x['id'] in ids]
    teachers = sort_by_rating(teachers)
    return render_template("index.html", teachers=teachers)


@app.route('/goal/<goal>/')
def goal(goal):
    teachers_by_goal = []
    has_changed = True
    with open('data.json') as f:
        goals = json.load(f)[0]
    with open('data.json') as f:
        data = json.load(f)[1]
        for teacher in data:
            if goal in teacher['goals']:
                teachers_by_goal.append(teacher)
    teachers_by_goal = sort_by_rating(teachers_by_goal)
    return render_template('goal.html', teachers=teachers_by_goal, goal=goals[goal])


@app.route('/profiles/<int:id>/')
def profile(id):
    goals = ""
    with open('data.json') as f:
        data = json.load(f)
    for temp_teacher in data[1]:
        if temp_teacher['id'] == id:
            teacher = temp_teacher
    for goal in teacher['goals']:
        goals += data[0][goal] + ", "
    return render_template('profile.html', teacher=teacher, goals=goals[:-2], days=days)


@app.route('/request/')
def request_():
    return render_template('request.html')


@app.route('/request_done/', methods=['POST'])
def request_done():
    goal = request.form.get('goal')
    time = request.form.get('time')
    name = request.form.get('u_name')
    phone = request.form.get('u_phone')
    with open('request.json') as f:
        data = json.load(f)
        data.append({'goal': goal, 'time': time, 'name': name, 'phone': phone})
    with open('request.json', 'w') as f:
        json.dump(data, f)
    with open('data.json') as f:
        data = json.load(f)
        goals = data[0]
    return render_template('request_done.html', goal=goal, time=time, name=name, phone=phone, goals=goals)


@app.route('/booking/<int:id>/<dotw>/<time>/')
def booking(id, dotw, time):
    with open('data.json') as f:
        teachers = json.load(f)[1]
        for temp_teacher in teachers:
            if temp_teacher['id'] == id:
                teacher = temp_teacher
    return render_template('booking.html', id=id, dotw=dotw, time=time, teacher=teacher, days=days)


@app.route('/booking_done/', methods=['POST'])
def booking_done():
    dotw = request.form.get('clientWeekday')
    time = request.form.get('clientTime')
    teacher_id = request.form.get('clientTeacher')
    name = request.form.get('clientName')
    phone = request.form.get('clientPhone')
    with open('booking.json') as f:
        data = json.load(f)
        data.append({'dotw': dotw, 'time': time, 'teacher_id': teacher_id, 'name': name, 'phone': phone})
    with open('booking.json', 'w') as file:
        json.dump(data, file)
    with open('data.json') as f:
        teachers = json.load(f)[1]
        for temp_teacher in teachers:
            if temp_teacher['id'] == int(teacher_id):
                teacher = temp_teacher
    return render_template('booking_done.html', dotw=dotw, time=time, name=name, phone=phone, teacher=teacher, days=days)


@app.route('/teachers')
def teachers_tab():
    with open('data.json') as f:
        data = json.load(f)[1]
    return render_template('teachers.html', teachers=data)


if __name__ == '__main__':
    app.run()
