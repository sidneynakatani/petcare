from app import app
import requests
import json
from flask import render_template, Flask, request, session, flash
from controller.login          import LoginController
from controller.forgotPassword import ForgotPassController
from controller.image   import ImageController
from controller.pet     import PetController
from controller.user    import UserController
from controller.message import MessageController
from dto.user           import User

@app.route('/access')
def access():
    login = LoginController()
    req = login.access(request)
    return render_template('index.html')



@app.route('/auth', methods=['POST'])
def auth():
    error = None
    pets  = []
    pet_list = []
    
    login = LoginController()
    req = login.auth(request)

    response = json.loads(req.text)
    print response
    auth = response['auth']
    name = response['name']
    code = response['code']
    
    if auth:

        req = getPets(code)
        list_pets = json.loads(req.text)

        message = MessageController()
        
        for pet in list_pets['pets']:
             pets.append( pet['image_id'])

        pet_list     = message.get(pets)
        message_size =  len(pet_list)

        session['logged_in'] = True
        session['pets_code'] = pets
        session['logged_name'] = name
        session['logged_code'] = code
        

	return render_template('dash.html', name = name, list_pets = list_pets, message_size = message_size, pet_list = pet_list)
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


@app.route('/updateUser', methods=['POST'])
def updateUser(): 
    usr = UserController()
    req = usr.updateUser(request)

    code = session['logged_code']
    req = getUser(code)
    user = json.loads(req.text)

    name = user['first_name']
    session['logged_name'] = name

    return render_template('profile.html', name = name, user = user)


@app.route('/updatePets', methods=['POST'])
def updatePets(): 
    pet = PetController()
    req = pet.updatePets(request)

    image = ImageController()
    image.updateImageStatus(request)
    
    name = session['logged_name']
    code = session['logged_code']

    req = getPets(code)
    list_pets = json.loads(req.text)
    
    return render_template('dash.html', name = name, list_pets = list_pets)

@app.route("/find", methods=['POST'])
def find():
    kind   = '^E_' + request.form['kind']
    images = getImagesByTags()
    return render_template('index.html', images = images, filter_enabled = True, kind = kind.strip())

@app.route("/addMessage", methods=['POST'])
def addMessage():
     messages = MessageController()
     messages.save(request)
     return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


def index():
    image  = ImageController()
    images = image.getImages(request)
    return render_template('index.html', images = images)

def getPets(user_code):
    pet = PetController()
    return pet.getPets(user_code)

def getUser(user_code):
    user = UserController()
    return user.getUser(user_code)

def getImagesByTags():
     image = ImageController()
     return image.getImageByTag(request)


