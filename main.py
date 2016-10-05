import os
import sys
import logging
from flask import render_template, Flask, request, session, flash


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


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

@app.route('/auth', methods=['POST'])
def auth():

    if request.form['password'] == 'password' and request.form['email'] == 'admin@admin.com':
        session['logged_in'] = True
	return render_template('dash.html')
    else:
        flash('wrong password!')

    return login()
    

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()


