from app import app
from flask import render_template, Flask, request, session


@app.route('/dash')
def dashBoard():
    if not session.get('logged_in'):
    	return index()

    return render_template('dash.html')

@app.route('/profile')
def profile():
    if not session.get('logged_in'):
    	return index()

    return render_template('profile.html')

@app.route('/add')
def add():
    if not session.get('logged_in'):
    	return index()

    return render_template('add.html')

@app.route('/config')
def config():
    if not session.get('logged_in'):
    	return index()

    return render_template('config.html')

@app.route('/message')
def message():
    if not session.get('logged_in'):
    	return index()

    return render_template('message.html')


def index():
    return render_template('login.html')


