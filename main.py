import os
from flask import render_template,Flask,request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run()


