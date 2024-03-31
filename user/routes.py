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

@app.route('/user/forgot_password', methods=['POST'])
def forgot_password():
    return User().forgot_password()

@app.route('/user/reset_password', methods=['POST'])
def reset_password():
    return User().reset_password()

@app.route('/user/save_training', methods=['POST'])
def save_training():
    return User().save_training()

@app.route('/user/update', methods=['POST'])
def update():
    return User().update()

@app.route('/user/clear_saved', methods=['POST', 'GET', 'DELETE', 'PUT', 'PATCH'])
def clear_saved():
    return User().clear_saved()
