from flask import Flask, render_template, redirect, url_for, session
from pymongo import MongoClient
import certifi
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'somesthing'
connection = "mongodb+srv://Danyil:m1MaJ0ADwtgm0mso@gymassistant.zuau6ap.mongodb.net/"
client = MongoClient(connection, tlsCAFile=certifi.where())

db = client['gymassistant']

all_exercises = db['all_exercises']
users_info=db['users']

from user import routes

@app.route('/')
def main_page():
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        trainings = all_exercises.find()
        return render_template('main_page.html', trainings=trainings, user_saved=user_saved)
    trainings = all_exercises.find()
    return render_template('main_page.html', trainings=trainings, user_saved=False)

@app.route('/my_profile/')
def my_profile():
    user_id = session['user']['_id']
    user_trainings = users_info.find_one({'_id': user_id})['trainings']
    names_of_saved = users_info.find_one({'_id': user_id})['trainings_name']
    user_data =  users_info.find_one({'_id': user_id})

    labels = []
    weights_data = []
    heights_data = []
    for info in user_data['info_statistic']:
        labels.append(info['timestamp'])
        weights_data.append(info['weight'])
        heights_data.append(info['height'])
    #     weights_data.append(int(info['weight']))
    #     heights_data.append(int(info['height']))

    # all_info = []

    # info_charts = user_data['info_statistic']
    # for obj in info_charts:
    #     all_info.append({'date': obj['timestamp'], 'weight': obj['weight'], 'height': obj['height']})

    return render_template('my_profile_extention.html', user_trainings=user_trainings, names_of_saved=names_of_saved, user_data=user_data,labels=labels, weights_data=weights_data, heights_data=heights_data)

@app.route('/update_parameters')
def update_parameters():
    return render_template('update_parameters.html')

@app.route('/my_training')
def my_training():
    return redirect(url_for('my_profile')+'#training')

@app.route('/all_trainings')
def all_trainings():
    trainings = all_exercises.find()
    return render_template('all_exerscises_page.html', trainings=trainings)


@app.route('/registration_form/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/login_form/')
def login_form():
    return render_template('login.html')

@app.route('/triceps')
def triceps():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи тріцепса", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи тріцепса", user_saved=False)

@app.route('/biceps')
def biceps():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи біцепса", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи біцепса", user_saved=False)

@app.route('/chest')
def chest():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Грудні м'язи", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Грудні м'язи", user_saved=False)

@app.route('/shoulders')
def shoulders():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Плечі і дельтовидні м'язи", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Плечі і дельтовидні м'язи", user_saved=False)

@app.route('/back_upper')
def back_upper():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Верхня частина спини і широкий м'яз спини", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Верхня частина спини і широкий м'яз спини", user_saved=False)

@app.route('/back_middle')
def back_middle():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Середина спини і поясничний відділ", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Середина спини і поясничний відділ", user_saved=False)

@app.route('/abs')
def abs():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Прес", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Прес", user_saved=False)

@app.route('/back_lower')
def back_lower():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Нижня частина спини", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Нижня частина спини", user_saved=False)

@app.route('/quads')
def quads():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи стегон", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи стегон", user_saved=False)

@app.route('/calves')
def calves():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи литок", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи литок", user_saved=False)

@app.route('/forearms')
def forearms():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Передпліччя", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Передпліччя", user_saved=False)

@app.route('/trapezium')
def trapezium():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Трапеція", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Трапеція", user_saved=False)

@app.route('/inner_thigh')
def inner_thigh():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "Внутрішні м'язи ніг", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Внутрішні м'язи ніг", user_saved=False)

@app.route('/mewing')
def mewing():
    trainings = all_exercises.find()
    if 'user' in session:
        user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
        return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи обличчя", user_saved=user_saved)
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи обличчя", user_saved=False)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
