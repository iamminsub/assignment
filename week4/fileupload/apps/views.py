from flask import render_template, Flask, request, url_for
from apps import app

from google.appengine.ext import db

class Photo(db.Model):
	image = db.BlobProperty()
	message = db.StringProperty()


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
	post_image = request.files['image']
	post_message = request.form['message']
	if post_image and allowed_file(post_image.filename):
		filestream = post_image.read()

		upload_data = Photo()
		upload_data.image = db.Blob(filestream)
		upload_data.message = post_message
		upload_data.put()

		comment = "Image and Comment are successfully uploaded!"

	else:
		comment = "Please upload valid image file"

	return render_template("upload.html", comment=comment, all_list=Photo.all())



@app.route('/show/<key>')
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data.image)
