from flask import render_template, Flask, request, url_for
from apps import app
import datetime
import time
from google.appengine.ext import db

class Photo(db.Model):
	message = db.StringProperty()
	date = db.DateTimeProperty(auto_now_add = True)

def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html", all_list=Photo.all())


@app.route('/upload', methods=['POST'])
def upload_db():
	
	post_message = request.form['message']

	upload_data = Photo()
	upload_data.message = post_message
	upload_data.date = datetime.datetime.now()
	upload_data.put()

	comment = "Your Comment is successfully uploaded!"

	return render_template("upload.html", comment=comment, all_list=Photo.all())
