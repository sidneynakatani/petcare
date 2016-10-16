import os
import sys
import logging
import requests
import json
from flask import render_template, Flask, request, session, flash


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

@app.route('/auth', methods=['POST'])
def auth():
    email = request.form['email']
    password = request.form['password']
    host = '{0}/login'.format(os.getenv('HOST'))
    
    if(os.getenv('HOST') == None):
        print  'Acesso local.'
	#host = 'http://127.0.0.1:5000/login'
        host = 'http://omegagls.herokuapp.com/login'
	
    req = requests.post(host, data={'email' : email, 'pass' : password} )

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
    

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()



if __name__ == '__main__':
    #app.debug = True
    #app.run(host='127.0.0.1', port=5001)
    app.run()


