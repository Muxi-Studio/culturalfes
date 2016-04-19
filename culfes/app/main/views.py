# coding: utf-8
from .. import app
from . import main
from ..models import Movie, Article, Photo, Anime, Course
from app import db
from flask import render_template, request, redirect, url_for, send_from_directory, flash, session
from geetest import GeetestLib
from werkzeug import secure_filename
import os
import random


captcha_id = app.config['CAPTCHA_ID']
private_key = app.config['PRIVATE_KEY']


def allowed_file(filename):
    if '.' in filename and \
            filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']:
                return True

@main.route('/')
def index():
    return render_template('/main/index.html')


@main.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        tag = request.form.get('tag')
        author_name = request.form.get('author_name')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if tag == 'movie':
                UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'movie')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Movie(
                        name=filename,
                        author_name=author_name,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'article':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'article')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Article(
                        name=filename,
                        author_name=author_name,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'photo':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'photo')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Photo(
                        name=filename,
                        author_name=author_name,
                        url=UPLOAD_FOLDER
                        )
            elif tag == 'anime':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'anime')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Anime(
                        name=filename,
                        url=UPLOAD_FOLDER,
                        author_name=author_name
                        )
            elif tag == 'course':
                UPLOAD_FOLDER = os.path.join(BUPLOAD_FOLDER, 'course')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                item = Course(
                        name=filename,
                        author_name=author_name,
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


@main.route('/rank/')
def rank():
    movies = Movie.query.all()
    articles = Article.query.all()
    animes = Anime.query.all()
    photos = Photo.query.all()
    courses = Course.query.all()
    sorted_movies = sorted(movies, key=lambda movie: movie.liked_count, reverse=True)
    sorted_animes = sorted(animes, key=lambda anime: anime.liked_count, reverse=True)
    sorted_articles = sorted(articles, key=lambda article: article.liked_count, reverse=True)
    sorted_photos = sorted(photos, key=lambda photo: photo.liked_count, reverse=True)
    sorted_courses = sorted(courses, key=lambda course: course.liked_count, reverse=True)
    return render_template('/main/rank.html', movies=sorted_movies, animes=animes, photos=photos, articles=articles, courses=courses)


@main.route('/movie/<int:id>/', methods=["GET", "POST"])
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    if request.method == 'POST':
        movie.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_movie'))
    return render_template('movie.html', movie=movie)


@main.route('/article/<int:id>/', methods=["GET", "POST"])
def get_article(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_article'))
    return render_template('article.html', article=article)


@main.route('/anime/<int:id>/', methods=["GET", "POST"])
def get_anime(id):
    anime = Anime.query.get_or_404(id)
    if request.method == 'POST':
        anime.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_anime'))
    return render_template('anime.html', anime=anime)


@main.route('/course/<int:id>/', methods=["GET", "POST"])
def get_course(id):
    course = Course.query.get_or_404(id)
    if request.method == 'POST':
        course.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_course'))
    return render_template('course.html', course=course)


@main.route('/photo/<int:id>/', methods=["GET", "POST"])
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    if request.method == 'POST':
        photo.liked_count += 1
        db.session.commit()
        flash("投票成功")
        return redirect(url_for('main.get_photo'))
    return render_template('photo.html', photo=photo)


@main.route('/captcha/')
def captcha():
    return render_template('/main/captcha.html')


@main.route('/getcaptcha/', methods=["GET"])
def get_captcha():
    user_id = random.randint(1,100)
    gt =  GeetestLib(captcha_id, private_key)
    status = gt.pre_process(user_id)
    session[gt.GT_STATUS_SESSION_KEY] = status
    session["user_id"] = user_id
    response_str = gt.get_response_str()
    return response_str


@main.route('/validate', methods=["POST"])
def validate_capthca():
    gt = GeetestLib(captcha_id, private_key)
    challenge = request.form[gt.FN_CHALLENGE]
    validate = request.form[gt.FN_VALIDATE]
    seccode = request.form[gt.FN_SECCODE]
    status = session[gt.GT_STATUS_SESSION_KEY]
    user_id = session["user_id"]
    if status:
        result = gt.success_validate(challenge, validate, seccode, user_id)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    result = "success" if result else "fail"
    if result == "success":
        return redirect(url_for("main.index"))
    else:
        flash("验证码错误!")
        return redirect(url_for("main.captcha"))
