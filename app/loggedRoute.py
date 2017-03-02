from app import app
from flask import render_template, Flask, request, session
from controller.pet import PetController
import json


@app.route('/dash')
def dashBoard():
    if not session.get('logged_in'):
    	return index()

    code = session['logged_code']
    name = session['logged_name']
    req = getPets(code)
    list_pets = json.loads(req.text)
        

    return render_template('dash.html', name = name, list_pets = list_pets)

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

def getPets(request):
    pet = PetController()
    return pet.getPets(request)


