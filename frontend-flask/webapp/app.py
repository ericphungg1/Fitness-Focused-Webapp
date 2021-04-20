from flask import Flask, render_template, request, jsonify
import requests
import json
import os
import initdb
import seng_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sign-in.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        jsdata = request.form['javascript_data']
        data = json.loads(jsdata)
        #should print in server terminal
        firstname = (data['fn'].replace('\xa0', '')).strip()
        email = (data['e'].replace('\xa0', '')).strip()
        password = (data['p'].replace('\xa0', '')).strip()
        print(firstname)
        print(email)
        print(password)
        #call this function
        #seng_db.newuser(firstname, lastname, email, password)
        return
    else:
        return render_template('sign-up.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/caloriecounter')
def calcount():
    return render_template('calorie_counter.html')

@app.route('/forum')
def forum():
    return render_template('community-forum.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('community-leaderboards.html')

@app.route('/fooddiary')
def fooddiary():
    return render_template('food_diary.html')

@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgot-password.html')

@app.route('/homepage', methods=['POST', 'GET'])
def homepage():
     if request.method == "POST":
        jsdata = request.form['javascript_data']
        data = json.loads(jsdata)
        #should print in server terminal
        if "w" in data:
            weight = (data['w'].replace('\xa0', '')).strip()
            print(weight)
            # add weight to db
        if "cal" in data:
            calories = (data['cal'].replace('\xa0', '')).strip()
            print(calories)
            #add cals to db
        if "wat" in data:
            water = (data['wat'].replace('\xa0', '')).strip()
            print(water)
            #add water to db
        return ""
     else:
        return render_template('home-page.html')


@app.route('/getmethod/<jsdata>')
def get_python_data():
    return json.dumps(sengdb.get)

@app.route('/createpost')
def createpost():
    return render_template('createpost.html')

@app.route('/personaltrainer')
def personaltrainer():
    return render_template('personal-trainer.html')

@app.route('/foodsearch')
def foodsearch():
    return render_template('foodsearch.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/recommendedexcercise')
def recommendedex():
    return render_template('recommended-exercise.html')

@app.route('/recommenderecipes')
def recommendedrec():
    return render_template('recommended-recipes.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

if __name__ == '__main__':
    #initialise database
    initdb.init()
    app.run(debug=True, host='0.0.0.0')
