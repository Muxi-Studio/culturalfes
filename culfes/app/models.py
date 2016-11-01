# coding: utf-8
"""
sql models

    use: Flask-SQLAlchemy
    -- http://flask-sqlalchemy.pocoo.org/2.1/

"""

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from wtforms.validators import Email
from datetime import datetime
from markdown import markdown
from flask import url_for, current_app
from app.exceptions import ValidationError
import bleach


# permissions
class Permission:
    """
    1. COMMENT: 0x01
    2. MODERATE_COMMENTS: 0x02
    3. ADMINISTER: 0x04
    """
    COMMENT = 0x01
    MODERATE_COMMENTS = 0x02
    ADMINISTER = 0x04


# user roles
class Role(db.Model):
    """
    1. User: COMMENT
    2. Moderator: MODERATE_COMMENTS
    3. Administrator: ADMINISTER
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT, True),
            'Moderator': (Permission.COMMENT |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (
                Permission.COMMENT |
                Permission.MODERATE_COMMENTS |
                Permission.ADMINISTER,
                False
            )
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    """user"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(164), unique=True, index=True)
    email = db.Column(db.String(164), info={'validator' : Email()})
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(164))

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def is_admin(self):
        if self.role_id == 2:
            return True
        return False

    def __repr__(self):
        return "<User %r>" % self.username


class AnonymousUser(AnonymousUserMixin):
    """ anonymous user """
    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser

class Base(object):
    id = db.Column(db.Integer, primary_key=True)
    upload_name = db.Column(db.Text)
    present_name = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    description = db.Column(db.Text)
    video_url = db.Column(db.Text)
    upload_url = db.Column(db.Text)
    a_time = db.Column(db.Text)
    author_name = db.Column(db.String(164))
    liked_count = db.Column(db.Integer, default=0)

    @staticmethod
    def on_changed_body(target, value, oldbalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))


class Movie(db.Model, Base):
    """movies"""
    __tablename__ = 'movies'
    tag = 'movie'

    def __repr__(self):
        return "<Movie %r>" % self.name


db.event.listen(Movie.body, 'set', Movie.on_changed_body)


class Anime(db.Model, Base):
    """animes"""
    __tablename__ = 'animes'
    tag = 'anime'

    def __repr__(self):
        return "<Anime %r>" % self.id


db.event.listen(Anime.body, 'set', Anime.on_changed_body)


class Article(db.Model, Base):
    """articles"""
    __tablename__ = 'articles'
    tag = 'article'

    def __repr__(self):
        return "<Article %r>" % self.id


db.event.listen(Article.body, 'set', Article.on_changed_body)


class Course(db.Model, Base):
    """courses"""
    __tablename__ = 'courses'
    tag = 'course'

    def __repr__(self):
        return "<Course %r>" % self.id


db.event.listen(Course.body, 'set', Course.on_changed_body)


class Photo(db.Model, Base):
    """photos"""
    __tablename__ = 'photos'
    tag = 'photo'

    def __repr__(self):
        return "<Photo %r>" % self.id


db.event.listen(Photo.body, 'set', Photo.on_changed_body)


class Startup(db.Model, Base):
    """startups"""
    __tablename__ = 'startups'
    tag = 'startup'

    def __repr__(self):
        return "<Startup %r>" % self.id


db.event.listen(Startup.body, 'set', Startup.on_changed_body)


class Notice(db.Model):
    """notices"""
    __tablename__ = 'notice'
    tag = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(164))
    appendix = db.Column(db.String(164))
    body = db.Column(db.Text)
    a_time = db.Column(db.Text)

    @staticmethod
    def on_changed_body(target, value, oldbalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    def __repr__(self):
        return "<Notice %r>" % self.id


class W_Movie(db.Model, Base):
    """w_movies"""
    __tablename__ = 'w_movies'
    tag = 'w_movie'

    def __repr__(self):
        return "<W_Movie %r>" % self.name


db.event.listen(W_Movie.body, 'set', W_Movie.on_changed_body)


class W_Anime(db.Model, Base):
    """w_animes"""
    __tablename__ = 'w_animes'
    tag = 'w_anime'

    def __repr__(self):
        return "<W_Anime %r>" % self.id


db.event.listen(W_Anime.body, 'set', W_Anime.on_changed_body)


class W_Article(db.Model, Base):
    """w_articles"""
    __tablename__ = 'w_articles'
    tag = 'w_article'

    def __repr__(self):
        return "<W_Article %r>" % self.id


db.event.listen(W_Article.body, 'set', W_Article.on_changed_body)


class W_Course(db.Model, Base):
    """w_courses"""
    __tablename__ = 'w_courses'
    tag = 'w_course'

    def __repr__(self):
        return "<W_Course %r>" % self.id


db.event.listen(W_Course.body, 'set', W_Course.on_changed_body)


class W_Photo(db.Model, Base):
    """w_photos"""
    __tablename__ = 'w_photos'
    tag = 'w_photo'

    def __repr__(self):
        return "<W_Photo %r>" % self.id

db.event.listen(W_Photo.body, 'set', W_Photo.on_changed_body)


class W_Startup(db.Model, Base):
    """w_startups"""
    __tablename__ = 'w_startups'
    tag = 'w_startup'

    def __repr__(self):
        return "<W_Startup %r>" % self.id


db.event.listen(W_Startup.body, 'set', W_Startup.on_changed_body)
