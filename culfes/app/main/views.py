# coding: utf-8
from .. import app
from . import main
from ..models import Movie, Article, Photo, Anime, Course, Startup, Notice
from ..models import W_Movie, W_Article, W_Photo, W_Anime, W_Course, W_Startup
from app import db, r1, r2, r3, r4, r5, r6
from flask import render_template, request, redirect, url_for, send_from_directory, flash, session
from geetest import GeetestLib
from werkzeug import secure_filename
import time
import os
import random


captcha_id = app.config['CAPTCHA_ID']
private_key = app.config['PRIVATE_KEY']
pic_appendix = app.config['PIC_APPENDIX']


def allowed_file(filename):
    if '.' in filename and \
            filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']:
                return True

@main.route('/')
def index():
    movies = Movie.query.all()
    courses = Course.query.all()
    animes = Anime.query.all()
    photos = Photo.query.all()
    startups = Startup.query.all()
    for eachPhoto in photos:
        eachPhoto.first_photo = eachPhoto.video_url.split(' ')[0]
    articles = Article.query.all()
    notices = Notice.query.all()
    return render_template(
            '/main/index.html',
            movies=movies[:3],
            courses=courses[:3],
            animes=animes[:3],
            photos=photos[:3],
            articles=articles[:3],
            notices=notices[:3],
            startups=startups[:3]
            )


@main.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        tag = request.form.get('upload-class-choice')
        file_name = request.form.get('file_name')
        description = request.form.get('description') or ''

        if not tag:
            flash("请选择类型!")
            return redirect(url_for('main.upload_file'))

        if not file_name:
            flash("请填写文件名!")
            return redirect(url_for('main.upload_file'))

        author_name = request.form.get('author_name')
        if not author_name:
            flash("请填写文件名!")
            return redirect(url_for('main.upload_file'))

        upload_url = request.form.get('upload_url')

        if not upload_url:
            file = request.files['file']
            if allowed_file(file.filename):
                filename = time.strftime("%a %b %d %H:%M:%S %Y",
                        time.localtime()) + ' ' + file_name + '.' + file.filename.rsplit('.', 1)[1]
            else:
                flash("请添加文件压缩包或链接!")
                return redirect(url_for('main.upload_file'))
        else:
            filename = time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()) + ' ' + file_name

        if tag == 'movie':
            UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'movie')
            if not upload_url:
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                UPLOAD_FOLDER = 'no'
            item = W_Movie(
                    upload_name=filename,
                    present_name=file_name,
                    author_name=author_name,
                    description=description,
                    upload_url=UPLOAD_FOLDER + filename,
                    video_url=upload_url,
                    a_time=(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))[:10]
                    )

        elif tag == 'article':
            if not upload_url:
                UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'article')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                UPLOAD_FOLDER = 'no'
            item = W_Article(
                    upload_name=filename,
                    present_name=file_name,
                    author_name=author_name,
                    description=desctiption,
                    upload_url=UPLOAD_FOLDER + filename,
                    video_url=upload_url,
                    a_time=(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))[:10]
                    )

        elif tag == 'photo':
            if not upload_url:
                UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'photo')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                UPLOAD_FOLDER = 'no'
            item = W_Photo(
                    upload_name=filename,
                    present_name=file_name,
                    author_name=author_name,
                    description=description,
                    upload_url=UPLOAD_FOLDER + filename,
                    video_url=upload_url,
                    a_time=(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))[:10]
                    )
        elif tag == 'anime':
            if not upload_url:
                UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'anime')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                UPLOAD_FOLDER = 'no'
            item = W_Anime(
                    upload_name=filename,
                    present_name=file_name,
                    author_name=author_name,
                    description=desctiption,
                    upload_url=UPLOAD_FOLDER + filename,
                    video_url=upload_url,
                    a_time=(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))[:10]
                    )
        elif tag == 'course':
            if not upload_url:
                UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'course')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                UPLOAD_FOLDER = 'no'
            item = W_Course(
                    upload_name=filename,
                    present_name=file_name,
                    author_name=author_name,
                    description=desctiption,
                    upload_url=UPLOAD_FOLDER + filename,
                    video_url=upload_url,
                    a_time=(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))[:10]
                    )
        elif tag == 'startup':
            if not upload_url:
                UPLOAD_FOLDER = os.path.join(app.config['BUPLOAD_FOLDER'], 'startup')
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                UPLOAD_FOLDER = 'no'
            item = W_Startup(
                    upload_name=filename,
                    present_name=file_name,
                    author_name=author_name,
                    description=desctiption,
                    upload_url=UPLOAD_FOLDER + filename,
                    video_url=upload_url,
                    a_time=(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))[:10]
                    )

        db.session.add(item)
        db.session.commit()
        flash("文件已上传!正在审核中···")
        return redirect(url_for('main.upload_file'))
    return render_template('/main/upload.html')


@main.route('/notices/')
def notices():
    notices = Notice.query.all()
    return render_template('/main/notices.html', notices=notices)


@main.route('/movies/')
def movies():
    movies = Movie.query.all()
    return render_template('main/movies.html', movies=movies)


@main.route('/animes/')
def animes():
    animes = Anime.query.all()
    return render_template('main/animes.html', animes=animes)


@main.route('/courses/')
def courses():
    courses = Course.query.all()
    return render_template('main/courses.html', courses=courses)


@main.route('/photos/')
def photos():
    photos = Photo.query.all()
    for eachPhoto in photos:
        eachPhoto.first_photo = eachPhoto.upload_url.split(' ')[0]
    return render_template('main/photos.html', photos=photos)


@main.route('/articles/')
def articles():
    articles = Article.query.all()
    return render_template('main/articles.html', articles=articles)


@main.route('/startups/')
def startups():
    startups = Startup.query.all()
    return render_template('main/startups.html', startups=startups)


@main.route('/rank/')
def rank():
    movies = Movie.query.all()
    articles = Article.query.all()
    animes = Anime.query.all()
    photos = Photo.query.all()
    courses = Course.query.all()
    startups = Startup.query.all()
    sorted_movies = sorted(movies, key=lambda movie: movie.liked_count, reverse=True)
    sorted_animes = sorted(animes, key=lambda anime: anime.liked_count, reverse=True)
    sorted_articles = sorted(articles, key=lambda article: article.liked_count, reverse=True)
    sorted_photos = sorted(photos, key=lambda photo: photo.liked_count, reverse=True)
    sorted_courses = sorted(courses, key=lambda course: course.liked_count, reverse=True)
    sorted_startups = sorted(startups, key=lambda startup: startup.liked_count, reverse=True)
    return render_template(
            'main/rank.html',
            movies=sorted_movies[:20],
            animes=sorted_animes[:20],
            photos=sorted_photos[:20],
            articles=sorted_articles[:20],
            courses=sorted_courses[:20],
            startups=sorted_startups[:20]
            )


@main.route('/movie/<int:id>/', methods=["GET", "POST"])
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    if 'vote' in session.keys():
        if session['vote'] == 1:
            ip = request.remote_addr
            if r1.get(ip):
                flash("每天只能投一次票!")
            else:
                movie.liked_count += 1
                db.session.add(movie)
                db.session.commit()
                flash("投票成功")
                r1.set(ip, ip)
            session['vote'] = 0
            return redirect(url_for('main.get_movie', id=movie.id))
    else:
        session['vote'] = 0
    return render_template('main/movie.html', movie=movie)


@main.route('/article/<int:id>/', methods=["GET", "POST"])
def get_article(id):
    article = Article.query.get_or_404(id)
    if 'vote' in session.keys():
        if session['vote'] == 1:
            ip = request.remote_addr
            if r2.get(ip):
                flash("每天只能投一次票!")
            else:
                article.liked_count += 1
                db.session.add(article)
                db.session.commit()
                flash("投票成功")
                r2.set(ip, ip)
            session['vote'] = 0
            return redirect(url_for('main.get_article', id=article.id))
    else:
        session['vote'] = 0
    return render_template('main/article.html', article=article)


@main.route('/anime/<int:id>/', methods=["GET", "POST"])
def get_anime(id):
    anime = Anime.query.get_or_404(id)
    anime_urls = anime.video_url.split(' ')

    # 根据文件后缀判断是图片还是视频
    if anime_urls[0].split('.')[-1] in pic_appendix or len(anime_urls[0].split('.')[-1]) > 5:
        flag = 'anime'
    else:
        flag = 'video'

    if 'vote' in session.keys():
        if session['vote'] == 1:
            ip = request.remote_addr
            if r3.get(ip):
                flash("每天只能投一次票!")
            else:
                anime.liked_count += 1
                db.session.add(anime)
                db.session.commit()
                flash("投票成功")
                r3.set(ip, ip)
            session['vote'] = 0
            return redirect(url_for('main.get_anime', id=anime.id))
    else:
        session['vote'] = 0
    return render_template('main/anime.html', anime=anime, flag=flag, anime_urls=anime_urls)


@main.route('/course/<int:id>/', methods=["GET", "POST"])
def get_course(id):
    course = Course.query.get_or_404(id)
    if 'vote' in session.keys():
        if session['vote'] == 1:
            ip = request.remote_addr
            if r4.get(ip):
                flash("每天只能投一次票!")
            else:
                course.liked_count += 1
                db.session.add(course)
                db.session.commit()
                flash("投票成功")
                r4.set(ip, ip)
            session['vote'] = 0
            return redirect(url_for('main.get_course', id=course.id))
    else:
        session['vote'] = 0
    return render_template('main/course.html', course=course)


@main.route('/photo/<int:id>/', methods=["GET", "POST"])
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    photo_urls = photo.video_url.split(' ')
    if 'vote' in session.keys():
        if session['vote'] == 1:
            ip = request.remote_addr
            if r5.get(ip):
                flash("每天只能投一次票!")
            else:
                photo.liked_count += 1
                db.session.add(photo)
                db.session.commit()
                flash("投票成功")
                r5.set(ip, ip)
            session['vote'] = 0
            return redirect(url_for('main.get_photo', id=photo.id))
    else:
        session['vote'] = 0
    return render_template('main/photo.html', photo=photo, photo_urls=photo_urls)


@main.route('/startup/<int:id>/', methods=["GET", "POST"])
def get_startup(id):
    startup = Startup.query.get_or_404(id)
    if 'vote' in session.keys():
        if session['vote'] == 1:
            ip = request.remote_addr
            if r6.get(ip):
                flash("每天只能投一次票!")
            else:
                startup.liked_count += 1
                db.session.add(startup)
                db.session.commit()
                flash("投票成功")
                r6.set(ip, ip)
            session['vote'] = 0
            return redirect(url_for('main.get_startup', id=startup.id))
    else:
        session['vote'] = 0
    return render_template('main/startup.html', startup=startup)


@main.route('/notice/<int:id>/')
def get_notice(id):
    notice = Notice.query.get_or_404(id)
    return render_template('main/notice.html', notice=notice)


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
    session['vote'] = 0
    gt = GeetestLib(captcha_id, private_key)
    challenge = request.form[gt.FN_CHALLENGE]
    validate = request.form[gt.FN_VALIDATE]
    seccode = request.form[gt.FN_SECCODE]
    status = session[gt.GT_STATUS_SESSION_KEY]
    user_id = session["user_id"]
    session['refer'] = request.referrer
    if status:
        result = gt.success_validate(challenge, validate, seccode, user_id)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    result = "success" if result else "fail"
    if result == "success":
        session['vote'] = 1
        return redirect(session['refer'])
    else:
        flash("验证码错误!")
        return redirect(session['refer'])
