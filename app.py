from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates', static_folder='static')
client = MongoClient("mongodb+srv://Danyil:m1MaJ0ADwtgm0mso@gymassistant.zuau6ap.mongodb.net/")
db = client['gymassistant']
users = db['users']

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/my_profile/')
def my_profile():
    return render_template('my_profile.html')

@app.route('/exercises/')
def exercises():
    return render_template('exercises.html')

if __name__ == '__main__':
    app.run(debug=True)
