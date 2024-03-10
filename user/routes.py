from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()

@app.route('/user/save_training', methods=['POST'])
def save_training():
    return User().save_training()

@app.route('/user/del_training', methods=['POST'])
def del_training():
    return User().del_training()

# @app.route('/save_picture', methods=['POST'])
# def profile_image():
#     return User().profile_image()

