from flask import Flask, render_template, redirect, url_for, session
from pymongo import MongoClient
import certifi

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
    return render_template('main_page.html', trainings=trainings)

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

@app.route('/registration_form/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/login_form/')
def login_form():
    return render_template('login.html')

@app.route('/triceps')
def triceps():
    trainings = all_exercises.find()
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи тріцепса", user_saved=user_saved)

@app.route('/biceps')
def biceps():
    trainings = all_exercises.find()
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи біцепса", user_saved=user_saved)

@app.route('/chest')
def chest():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Грудні м'язи", user_saved=user_saved)

@app.route('/shoulders')
def shoulders():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Плечі і дельтовидні м'язи", user_saved=user_saved)

@app.route('/back_upper')
def back_upper():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Верхня частина спини і широкий м'яз спини", user_saved=user_saved)

@app.route('/back_middle')
def back_middle():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Середина спини і поясничний відділ", user_saved=user_saved)

@app.route('/abs')
def abs():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи пресу", user_saved=user_saved)

@app.route('/back_lower')
def back_lower():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Тазобедренний суглоб", user_saved=user_saved)

@app.route('/quads')
def quads():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи тазу і квадріцепсу", user_saved=user_saved)

@app.route('/calves')
def calves():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "М'язи литок", user_saved=user_saved)

@app.route('/forearms')
def forearms():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Передпліччя", user_saved=user_saved)

@app.route('/trapezium')
def trapezium():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Трапеція", user_saved=user_saved)

@app.route('/inner_thigh')
def inner_thigh():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Внутрішні м'язи ніг", user_saved=user_saved)

@app.route('/mewing')
def mewing():
    user_saved = users_info.find_one({'_id': session['user']['_id']})['trainings_name']
    trainings = all_exercises.find()
    return render_template('exercises_extention.html', trainings=trainings, muscle = "Обличчя", user_saved=user_saved)


if __name__ == '__main__':
    app.run(debug=True)
