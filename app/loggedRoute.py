from app import app
from flask import render_template, Flask, request, session
from controller.pet import PetController
from controller.user import UserController
from controller.message import MessageController

import json


@app.route('/dash')
def dashBoard():
    if not session.get('logged_in'):
    	return index()

    code = session['logged_code']
    name = session['logged_name']
    req = getPets(code)
    list_pets = json.loads(req.text)
    
    
    pets  = []
        
    for pet in list_pets['pets']:
         pets.append( pet['image_id'])    

    message = MessageController()
    message_size = message.count(pets)

    pet_list = []
    pet_list = message.get(pets)

    return render_template('dash.html', name = name, list_pets = list_pets, message_size = message_size, pet_list = pet_list)

@app.route('/profile')
def profile():
    if not session.get('logged_in'):
    	return index()

    code = session['logged_code']
    name = session['logged_name']
    req = getUser(code)
    user = json.loads(req.text)

    return render_template('profile.html', name = name, user = user)

@app.route('/add')
def add():
    if not session.get('logged_in'):
    	return index()

    name = session['logged_name']

    return render_template('add.html', name = name)

@app.route('/config')
def config():
    if not session.get('logged_in'):
    	return index()

    name = session['logged_name']

    return render_template('config.html', name = name)

@app.route('/message')
def message():
    if not session.get('logged_in'):
    	return index()

    name = session['logged_name']

    return render_template('message.html', name = name)


def index():
    return render_template('login.html')


def getPets(user_code):
    pet = PetController()
    return pet.getPets(user_code)


def getUser(user_code):
    user = UserController()
    return user.getUser(user_code)




