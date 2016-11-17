import os
import sys
import logging
import requests
import json
from flask import render_template, Flask, request, session, flash
from controller.login import LoginController


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/access')
def access():
    hashId = request.args.get('id')
    print hashId
    return render_template('index.html')

@app.route('/dash')
def dashBoard():
    if not session.get('logged_in'):
    	return login()

    return render_template('dash.html')

@app.route('/profile')
def profile():
    if not session.get('logged_in'):
    	return login()

    return render_template('profile.html')

@app.route('/add')
def add():
    if not session.get('logged_in'):
    	return login()

    return render_template('add.html')

@app.route('/config')
def config():
    if not session.get('logged_in'):
    	return login()

    return render_template('config.html')

@app.route('/message')
def message():
    if not session.get('logged_in'):
    	return login()

    return render_template('message.html')

@app.route('/auth', methods=['POST'])
def auth():
    
    login = LoginController()
    req = login.auth(request)

    response = json.loads(req.text)
    auth = response['auth']
    name = response['name']

    if auth:
        session['logged_in'] = True
        session['logged_name'] = name
	return render_template('dash.html', name = name)
    else:
        flash('wrong password!')

    return login()

@app.route('/register', methods=['POST'])
def register():
    
    login = LoginController()
    req = login.register(request)

    #FIXME Verify why dont work
    #response = json.loads(req.text)
    #status = response['status']
    #print status

    return render_template('login.html')   

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()



if __name__ == '__main__':
    #app.debug = True
    #app.run(host='127.0.0.1', port=5001)
    app.run()


