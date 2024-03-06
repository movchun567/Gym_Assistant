from flask import Flask, jsonify, request, render_template
import uuid
from passlib.hash import pbkdf2_sha256
from app import db

class User:
    def signup(self):
        print(request.form)

        user = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "password" : request.form.get('password_1'),
            "bdate" : request.form.get('bdate'),
            "gender" : request.form.get('gender'),
            "weight" : request.form.get('weight'),
            "height" : request.form.get('height')
        }
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db['users'].find_one({"email" : user['email']}):
            return jsonify({"error" : "Email address already in use"}), 400

        if db['users'].insert_one(user):
            return render_template('main_page.html')

        return jsonify({"error" : "Signup failed"}), 400
