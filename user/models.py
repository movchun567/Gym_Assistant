from flask import Flask, jsonify, request, render_template, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
from app import db

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
            "height" : request.form.get('height')
        }
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db['users'].find_one({"email" : user['email']}):
            return jsonify({"error" : "Email address already in use"}), 400

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

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({"error" : "Invalid login credentials"}), 401
