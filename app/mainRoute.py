from app import app
from flask import render_template


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

@app.route('/forgot')
def forgot():
    return render_template('forgotPass.html')

@app.route('/changePassword')
def changePassword():
    return render_template('changePassword.html')
