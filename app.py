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

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'GET':

		return render_template('sign_up.html')
	else:
		new_username = request.form.get("username")
		new_password = request.form.get("password")
		new_interests = request.form.get("interests")
		new_bio = request.form.get("bio")
		new_gender = request.form.get("gender") 
		new_picture = request.form.get("picture")
		new_username = User(username = new_username, password = new_password, interests = new_interests, bio = new_bio, gender = new_gender, picture = new_picture)	 
		session.add(new_username)
		session.commit()
		return redirect(url_for("home"))	
	

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

@app.route('/sign_in', methods = ['GET', 'POST'])
def sign_in():
	if request.method == 'GET':
		return render_template('sign_in.html')
	else:
		username_data=request.form.get("UserName")
		password     =request.form.get("Password")
		user  =session.query(User).filter_by(username=username_data).first()
		db_password = user.password
		print("          printing password",password,db_password)
		if password == db_password:
			print("GOT TO HERE")
			return render_template('profile.html', profile = user)
		else:
			print("incorrect password")
			return render_template('sign_in.html')
			
		
	


@app.route('/profile/<int:profile_id>')
def profile(profile_id):
	profile = session.query(User).filter_by(id=profile_id).first()
	return render_template('profile.html', profile = profile)

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