from app import app
import requests
import json
from flask import render_template, Flask, request, session, flash
from controller.login import LoginController
from controller.forgotPassword import ForgotPassController
from controller.image import ImageController
from dto.user import User

@app.route('/access')
def access():
    login = LoginController()
    req = login.access(request)
    return render_template('index.html')



@app.route('/auth', methods=['POST'])
def auth():
    error = None
    
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
        error = 'Login ou Senha invalidos'

    return render_template('login.html', error = error)



@app.route('/register', methods=['POST'])
def register():
    login = LoginController()
    req = login.register(request)
    return render_template('login.html')   


@app.route('/forgotPass', methods=['POST'])
def forgotPass():
    changePass = ForgotPassController()
    req = changePass.change(request)
    email = request.form['email']
    return render_template('forgotPassRequested.html', email = email)

@app.route('/validatePassword', methods=['POST'])
def validatePassword():
    password = ForgotPassController()
    user = password.update(request)


    if user.status:
         session['logged_in'] = True
         session['logged_name'] = user.name
         return render_template('dash.html', name = user.name)

    else:
         print 'Nao foi possivel atualizar registro.'
         error = 'O token enviado ja foi utilizado'       
  
    return render_template('changePassword.html', error = error)

@app.route('/upload', methods=['POST'])
def upload():
    image = ImageController()
    req = image.upload(request)
    return render_template('add.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


def index():
    return render_template('index.html')




