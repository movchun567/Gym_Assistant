from flask import Flask, jsonify, request, render_template, session, redirect, url_for, abort, flash
import uuid
from passlib.hash import pbkdf2_sha256
from app import db
import datetime
import smtplib

users = db['users']
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

class User:
    def start_session(self, user):
        session['logged_in'] = True
        session['user'] = user
        return redirect('/my_profile')

    def signup(self):
        print(request.form)

        user = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "password" : request.form.get('password_1'),
            "gender" : request.form.get('gender'),
            "weight" : request.form.get('weight'),
            "height" : request.form.get('height'),
            "trainings_name": [],
            "trainings":[],
            "info_statistic": [{"weight" :request.form.get('weight'), "height" : request.form.get('height'), 'timestamp': datetime.datetime.now().strftime("%d.%m.%Y")}]
        }
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db['users'].find_one({"email" : user['email']}):
            error_message = "Пошта вже використовується"
            return render_template('registration_form.html', error_message=error_message)

        if db['users'].insert_one(user):
            return self.start_session(user)

        return jsonify({"error" : "Signup failed"}), 400
    
    def forgot_password(self):
        global TMP_PWD
        global USER 
        TMP_PWD = str(uuid.uuid4().hex)
        USER = db['users'].find_one({
            "email" : request.form.get('email')
        })
        server.login("gymassistanthelp@gmail.com", 'cvow rpib jrzd ulkp')
        msg = 'Subject: Temporary code to reset your password\n\n' + "Please, enter this code into the reset form: " + TMP_PWD \
            + "\nIf you didn't request a password reset, please ignore this email. \n\nBest regards, \nGym Assistant team."
        if USER:
            server.sendmail("gymassistanthelp@gmail.com", USER['email'], msg)
            return redirect('/reset_form')
        if not USER:
            error_message = "Такого користувача не існує"
            return render_template('forgot_form.html', error_message=error_message)
        
        return jsonify({"error" : "Invalid email"}), 400
    
    def reset_password(self):
        if request.form.get('temp_code') != TMP_PWD and request.form.get('password_1') != request.form.get('password_2'):
            error_message = "Тимчасовий код та паролі не співпадають"
            return render_template('reset_form.html', error_message=error_message)
        elif request.form.get('temp_code') != TMP_PWD:
            error_message = "Неправильний тимчасовий код"
            return render_template('reset_form.html', error_message=error_message)
        elif request.form.get('password_1') != request.form.get('password_2'):
            error_message = "Паролі не співпадають"
            return render_template('reset_form.html', error_message=error_message)
        USER['password'] = pbkdf2_sha256.encrypt(request.form.get('password_1'))
        db['users'].update_one({'_id': USER['_id']}, {'$set': {'password': USER['password']}})
        return redirect('/login_form')

    
    def signout(self):
        session.clear()
        return redirect('/')
    
    def login(self):
        user = db['users'].find_one({
            "email" : request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password_1'), user['password']):
            return self.start_session(user)

        error_message = "Неправильна пошта або пароль"
        return render_template('login.html', error_message=error_message)
    
    def save_training(self):
        if 'user' not in session:
            # abort(401, description="Please, log in first")
            # return jsonify({'error': 'not_logged_in'}), 401
            flash('Please, log in first')
            return '', 204

        user_id = session['user']['_id'] # query to find the user's document)
        if request.form.get('training_name') in users.find_one({'_id': user_id})['trainings_name']:
            users.update_one({'_id': user_id},  # query to find the user's document
            {'$pull': {'trainings_name': request.form.get('training_name')}})  # update operation
            users.update_one({'_id': user_id},
            {'$pull': {'trainings': { 'training_url': request.form.get('training_url'), 'training_name': request.form.get('training_name'), 'training_description': request.form.get('training_description')}}})
            return '', 204
        users.update_one({'_id': user_id},  # query to find the user's document
        {'$push': {'trainings_name': request.form.get('training_name')}})  # update operation
        users.update_one({'_id': user_id},
        {'$push': {'trainings': { 'training_url': request.form.get('training_url'), 'training_name': request.form.get('training_name'), 'training_description': request.form.get('training_description')}}})
        return '', 204


    
    #     # convert the image data to a Base64 string
    #     # base64_string = base64.b64encode(contents).decode('utf-8')
    #     users.update_one({'_id': user_id},
    #     {'$set': {'profile_image': request.form.get('profile_image')}})
    #     return '', 204
    
    def update(self):
        user_id = session['user']['_id']

        new_weight = request.form.get('weight')
        new_height = request.form.get('height')
        # Update the user's profile with the new weight and height
        users.update_one({'_id': user_id}, {'$set': {'weight': new_weight, 'height': new_height}})
        # Add a new entry to the historical data
        users.update_one({'_id': user_id}, {'$push':{'info_statistic': {'weight': new_weight, 'height': new_height, 'timestamp': datetime.datetime.now().strftime("%d.%m.%Y")}}})

        users.update_one({'_id': user_id},
        {'$set':  {'weight': request.form.get('weight'), 'height': request.form.get('height')}})
        return redirect(url_for('my_profile'))
    
    def clear_saved(self):
        user_id = session['user']['_id']
        users.update_one({'_id': user_id},
        {'$set': {'trainings_name': [], 'trainings': []}})
        return redirect(url_for('my_profile'))
