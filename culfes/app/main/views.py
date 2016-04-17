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
        athor_name = request.form.get('author_name')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if tag == 'movie':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'movie')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Movie(
                        name=filename,
                        author_name=author_name
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'article':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'article')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Article(
                        name=filename,
                        author_name=author_name
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'photo':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'photo')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Photo(
                        name=filename,
                        author_name=author_name
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'anime':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'anime')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Anime(
                        name=filename,
                        url=UPLOAD_FOLDER
                        author_name=author_name
                        )
            elif tag == 'course':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'course')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Course(
                        name=filename,
                        author_name=author_name
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


@main.route('/movies/')
def movies():
    movies = Movie.query.all()
    return render_template('items.html', movies=movies)


@main.route('/articles/')
def articles():
    articles = Article.query.all()
    return render_template('items.html', articles=articles)


@main.route('/courses/')
def courses():
    courses = Courses.query.all()
    return render_template('items.html', courses=courses)


@main.route('/animes/')
def animes():
    animes = Anime.query.all()
    return render_template('items.html', animes=animes)


@main.route('/photos/')
def photos():
    photos = Photo.query.all()
    return render_template('items.html', photos=photos)


@main.route('/movie/<int:id>/')
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    if request.method == 'POST':
        movie.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_movie'))
    return render_template('movie.html', movie=movie)


@main.route('/article/<int:id>/')
def get_article(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_article'))
    return render_template('article.html', article=article)


@main.route('/anime/<int:id>/')
def get_anime(id):
    anime = Anime.query.get_or_404(id)
    if request.method == 'POST':
        anime.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_anime'))
    return render_template('anime.html', anime=anime)


@main.route('/course/<int:id>/')
def get_course(id):
    course = Course.query.get_or_404(id)
    if request.method == 'POST':
        course.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_course'))
    return render_template('course.html', course=course)


@main.route('/photo/<int:id>/')
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    if request.method == 'POST':
        photo.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_photo'))
    return render_template('photo.html', photo=photo)
