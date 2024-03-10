from flask import Flask, jsonify, request, render_template, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
from app import db
import gridfs
import base64

users = db['users']

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
            "profile_image": {}
        }
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db['users'].find_one({"email" : user['email']}):
            error_message = "Пошта вже використовується"
            return render_template('registration_form.html', error_message=error_message)

        if db['users'].insert_one(user):
            return self.start_session(user)

        return jsonify({"error" : "Signup failed"}), 400
    
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
        user_id = session['user']['_id'] # query to find the user's document)
        users.update_one({'_id': user_id},  # query to find the user's document
        {'$push': {'trainings_name': request.form.get('training_name')}})  # update operation
        users.update_one({'_id': user_id},
        {'$push': {'trainings': { 'training_name': request.form.get('training_name'), 'training_description': request.form.get('training_description')}}})
        return '', 204
    
    def del_training(self):
        user_id = session['user']['_id']
        users.update_one({'_id': user_id},  # query to find the user's document
        {'$pull': {'trainings_name': request.form.get('training_name')}})  # update operation
        users.update_one({'_id': user_id},
        {'$pull': {'trainings': { 'training_name': request.form.get('training_name'), 'training_description': request.form.get('training_description')}}})
        return '', 204
    
    def profile_image(self):
        # fs = gridfs.GridFS(db)
        user_id = session['user']['_id']
        # file = request.form.get('profile_image')
        # file = fs.get_last_version(filename="file")
        # contents = file.read()

    # convert the image data to a Base64 string
        # base64_string = base64.b64encode(contents).decode('utf-8')
        users.update_one({'_id': user_id},
        {'$set': {'profile_image': request.form.get('profile_image')}})
        return '', 204
