from flask import Flask, render_template, redirect, session, url_for
from functools import wraps
from pymongo import MongoClient
import certifi

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'somesthing'
connection = "mongodb+srv://Danyil:m1MaJ0ADwtgm0mso@gymassistant.zuau6ap.mongodb.net/"
client = MongoClient(connection, tlsCAFile=certifi.where())

db = client['gymassistant']

all_exercises = db['all_exercises']

from user import routes

# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             return redirect('/')
#     return wrap

@app.route('/')
def main_page():
    return render_template('main_page.html')

# @app.route('/my_profile/')
# @login_required
# def my_profile():
#     return render_template('my_profile.html')


@app.route('/my_profile/')
def my_profile():
    return render_template('my_profile.html')

@app.route('/my_training')
def my_training():
    return redirect(url_for('my_profile')+'#training')

@app.route('/registration_form/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/login_form/')
def login_form():
    return render_template('login.html')

@app.route('/triceps')
def triceps():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи тріцепса")

@app.route('/biceps')
def biceps():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи біцепса")

@app.route('/chest')
def chest():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Грудні м'язи")

@app.route('/shoulders')
def shoulders():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Плечі і дельтовидні мязи")

@app.route('/back_upper')
def back_upper():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Верхня частина спини і широкий м'яз спини")

@app.route('/back_middle')
def back_middle():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Середина спини і поясничний відділ")

@app.route('/abs')
def abs():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи пресу")

@app.route('/back_lower')
def back_lower():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Тазобедренний суглоб")

@app.route('/quads')
def quads():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи тазу і квадріцепсу")

@app.route('/calves')
def calves():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи ікри")

@app.route('/forearm')
def forearm():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Передпліччя")

@app.route('/trapezium')
def trapezium():
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Трапеція")

if __name__ == '__main__':
    app.run(debug=True)
