from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/goals/<goal>/')
def goal():
    return render_template('goal.html')


@app.route('/profiles/<id>/')
def profile(id):
    return render_template('profile.html')


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
