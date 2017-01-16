import os
import sys
import logging
from flask import Flask


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
from app import mainRoute, loggedRoute, businessRoute









