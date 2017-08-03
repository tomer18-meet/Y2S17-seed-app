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
	videos = session.query(Video).all()
	return render_template('index.html', videos = videos)

@app.route('/sign_up')
def sign_up():
    
    return render_template('sign_up.html')

@app.route('/categories')
def categories():
	return render_template('categories.html')

@app.route('/categories/<string:cat>')
def selected_category(cat):
	#videos = session.query(Video).filter_by(category=cat).all()
    videos = session.query(Video).filter_by(category=cat).all()
    return render_template('category.html', videos = videos, cat=cat)

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

@app.route('/add_video', methods = ['GET', 'POST'])
def add_video():
	if request.method == 'GET':

		return render_template('add_video.html')
	else:
		video_url = request.form.get("video_url")
		post_user = request.form.get("username")
		post_cat = request.form.get("category")
		new_video = Video(video = video_url, 
			username = post_user, 
			category = post_cat)
		session.add(new_video)
		session.commit()
		return redirect(url_for("home"))