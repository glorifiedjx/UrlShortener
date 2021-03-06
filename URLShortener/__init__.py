#!/usr/bin/python3
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'URLShorterner.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SERVER_NAME'] = ""
app.config['DEBUG'] = True
db = SQLAlchemy(app)


import URLShortener.models
import URLShortener.views
