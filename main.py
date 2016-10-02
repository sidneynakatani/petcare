import os
from flask import render_template,Flask,request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/pricing.html')
def pricing():
    return render_template('pricing.html')

@app.route('/dash')
def dashBoard():
    return render_template('dash.html')


if __name__ == '__main__':
    app.run()


