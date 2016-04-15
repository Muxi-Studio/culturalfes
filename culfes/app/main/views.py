# coding: utf-8
from . import main
from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = '/Users/kasheemlew/Downloads/upload'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'avi']

def allowed_file(filename):
    if '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS:
                return True

@main.route('/')
def index():
    return render_template('/main/index.html')


@main.route('/up/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('main.upload_file', filename=filename))
    return render_template('/main/upload_file.html')


@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)
