from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app config
app.config['SECRET_KEY'] = 'this is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python:1111!@localhost/python_db?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from models import *

db.create_all()
print(db)


@app.route('/')
@app.route('/index')
def index():
    #return 'Hello Flask!'
    # return '''<!DOCTYPE HTML><html>
    #   <head>
    #     <title>Flask app</title>
    #   </head>
    #   <body>
    #     <h1>Hello Flask!</h1>
    #   </body>
    # </html>'''
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
  #return 'About 페이지'
  return render_template('about.html', title='About')
