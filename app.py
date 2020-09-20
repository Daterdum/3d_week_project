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
def request():
    return render_template('request.html')


@app.route('/request_done/')
def request_done():
    return render_template('request_done.html')


@app.route('/booking/<id>/<dotw>/<time>/')
def booking(id, dotw, time):
    return render_template('booking.html')


@app.route('/booking_done/')
def booking_done():
    return render_template('booking_done.html')


if __name__ == '__main__':
    app.run()
