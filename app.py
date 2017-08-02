# flask imports
from flask import Flask, render_template, request, redirect, url_for
# SQLAlchemy
from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/categories/<string:cat>')
def selected_category(cat):
	videos = session.query(Video).filter_by(category=cat).all()
    return render_template('category.html', videos = videos, cat = cat)

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/profile')
def profile(id):
   # profile = session.query(User).filter_by(id=id).first()
    return render_template('profile.html', profile=profile )

