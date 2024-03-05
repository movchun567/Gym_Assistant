from flask import Flask, request, render_template, redirect, url_for
from urllib.parse import urlparse
# from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import certifi
ca = certifi.where()

# uri = "mongodb://localhost:27017"
uri = "mongodb+srv://Maria:rE6DfRl4DCkePiYl@gymassistant.zuau6ap.mongodb.net/?retryWrites=true&w=majority&appName=GymAssistant"

client = MongoClient(uri, tlsCAFile=certifi.where())

app = Flask(__name__)

db = client['gymassistant']
# app.secret_key = 'your_secret_key'
# all_videos = db.saved
# personal_videos = db.personal
# db = client.gymassistant

all_videos = db.all_exercises
personal_videos = db.personal

user_info = db.users

# @app.route('/')
# def home():
#     saved_trainings = all_videos.find()
#     return render_template('my_p.html', saved_trainings=saved_trainings)

@app.route('/shoulders_delta')
def shoulders_delta():
    saved_trainings = all_videos.find()
    return render_template('extention.html', saved_trainings=saved_trainings, muscle = 'Плечі і дельтовидні мязи')

@app.route('/chest')
def chest():
    saved_trainings = all_videos.find()
    return render_template('extention.html', saved_trainings=saved_trainings, muscle = "Грудні м'язи")

@app.route('/triceps')
def triceps():
    saved_trainings = all_videos.find()
    return render_template('extention.html', saved_trainings=saved_trainings, muscle = 'Тріцепс')

@app.route('/')
def home():
    saved_trainings = personal_videos.find()
    user = user_info.find()
    return render_template('my_profile.html', saved_trainings=saved_trainings, user = user)

@app.route('/my_profile')
def my_profile():
    user = db.users.find({'name': 'Bob Wood'})

    saved_trainings = personal_videos.find()
    return render_template('my_profile.html', saved_trainings=saved_trainings,  user = user)

@app.route('/save', methods=['POST'])
def save():
    video_url = request.form.get('video_url')
    name = request.form.get('name')
    description = request.form.get('description')

    referrer_url = request.referrer
    referrer_path = urlparse(referrer_url).path
    already_saved = personal_videos.find_one({'name': name})
    not_yet = all_videos.find_one({'name': name})
    if already_saved:
        all_videos.update_one({'_id': not_yet['_id']}, {'$set': {'bookmarked': False}})
        personal_videos.delete_one({'_id': already_saved['_id']})
    else:
        new_content = {'name': name, 'video_url': video_url, 'description': description, 'bookmarked': True}
        all_videos.update_one({'_id': not_yet['_id']}, {'$set': {'bookmarked': True}})
        personal_videos.insert_one(new_content)

    return redirect(referrer_path)

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form.get('name')

    referrer_url = request.referrer
    referrer_path = urlparse(referrer_url).path
    already_saved = personal_videos.find_one({'name': name})
    not_yet = all_videos.find_one({'name': name})
    all_videos.update_one({'_id': not_yet['_id']}, {'$set': {'bookmarked': False}})
    personal_videos.delete_one({'_id': already_saved['_id']})

    return redirect(referrer_path)

if __name__ == "__main__":
    app.run(debug=True)
