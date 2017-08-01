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
def IDeAS():
    #show_mainpage(mostrecent)
    return render_template('index.html')

@app.route('/categories')
def show_category_mainpage():
	render_template('my_categories.html')

@app.route('/categories/<string:catname>')
def show_category(catname):
	return render_template('category.html')

@app.route('/categories/sub/<string:subcatname>')
def show_category_2(name):
	return render_template()	

