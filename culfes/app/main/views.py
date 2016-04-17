# coding: utf-8
from . import main
from ..models import Movie, Article, Photo, Anime, Course
from app import db
from flask import render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug import secure_filename
import os

BUPLOAD_FOLDER = '/Users/kasheemlew/Downloads/upload'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'avi']

def allowed_file(filename):
    if '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS:
                return True

@main.route('/')
def index():
    return render_template('/main/index.html')


@main.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        tag = request.form.get('tag')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if tag == 'movie':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'movie')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Movie(
                        name=filename,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'article':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'article')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Article(
                        name=filename,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'photo':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'photo')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Photo(
                        name=filename,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'anime':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'anime')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Anime(
                        name=filename,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'course':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'course')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Course(
                        name=filename,
                        url=UPLOAD_FOLDER
                        )
        else:
            flash("Bad File!")
            return redirect(url_for('main.upload_file'))
        db.session.add(item)
        db.session.commit()
        flash("文件已上传")
        return redirect(url_for('main.upload_file'))
    return render_template('/main/upload_file.html')
