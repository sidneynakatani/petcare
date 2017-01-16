from app import app
import requests
import json
from flask import render_template, Flask, request, session, flash
from controller.login import LoginController
from controller.forgotPassword import ForgotPassController


@app.route('/access')
def access():
    login = LoginController()
    req = login.access(request)
    return render_template('index.html')



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

    return render_template('login.html')



@app.route('/register', methods=['POST'])
def register():
    login = LoginController()
    req = login.register(request)
    return render_template('login.html')   




@app.route('/forgotPass', methods=['POST'])
def forgotPass():
    changePass = ForgotPassController()
    req = changePass.change(request)
    return render_template('index.html')



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


def index():
    return render_template('index.html')




