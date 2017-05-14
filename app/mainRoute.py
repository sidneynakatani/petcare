from app import app
from flask import render_template, request
from controller.image import ImageController


@app.route("/")
def index():
    images = getImages()
    return render_template('index.html', images = images, filter_enabled = False)

@app.route("/find", methods=['POST'])
def find():
    kind   = request.form['kind']
    images = getImagesByTags()
    return render_template('index.html', images = images, filter_enabled = True, kind = kind )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/forgot')
def forgot():
    return render_template('forgotPass.html')

@app.route('/changePassword')
def changePassword():
    return render_template('changePassword.html')


def getImages():
     image = ImageController()
     return image.getImages(request)

def getImagesByTags():
     image = ImageController()
     return image.getImageByTag(request)

