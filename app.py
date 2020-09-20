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


@app.route('/')
def index():
    ids = sample(range(11), k=3)
    teachers = []
    with open('data.json') as f:
        temp_teachers = json.load(f)[1]
        print(temp_teachers)
        teachers = [x for x in temp_teachers if x['id'] in ids]
    return render_template("index.html", teachers=teachers)


@app.route('/goals/<goal>/')
def goal():
    return render_template('goal.html')


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
def request_edu():
    return render_template('request.html')


@app.route('/request_done/')
def request_done():
    return render_template('request_done.html')


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


if __name__ == '__main__':
    app.run()
