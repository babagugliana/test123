# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from fileinput import filename
import imp
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from flask import Flask, render_template, request, jsonify
from apps.config import API_GENERATOR
import traceback

@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index', API_GENERATOR=len(API_GENERATOR))

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, API_GENERATOR=len(API_GENERATOR))

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
        
        
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

@blueprint.route('/upload', methods=['POST'])
def upload_picture():
    if 'picture' in request.files:
        print(1)
        picture = request.files['picture']

        # Check if the file has an allowed extension
        if allowed_file(picture.filename):
            print(2)
            filename = secure_filename(picture.filename)
            picture.save('pictures/' + filename)
            return "Picture uploaded successfully!", 200
        else:
            print(3)
            return "File extension not allowed. Please upload a .jpg, .jpeg, or .png file.", 400
    print(4)
    return "No picture received!", 400

def allowed_file(filename):
    print(5)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/test', methods=['POST'])
def test():
    print("hello")
    print(request.form)
    """Handles contact me form to decide if user is allowed to contact me."""
    if request.form['dropdown1'] == "" or request.form['dropdown2'] == "" or \
        request.form['dropdown3'] == "" or request.form['dropdown4'] == "" or \
        request.form['dropdown5'] == "":
        return render_template("home/newnew.html", message="You cannot leave fields blanks DAWG", show_message=True)
    else:
        print(request.form)
        return render_template("home/newnew.html", message="YEP THATS LEGIT DAWG", show_message=True)


@blueprint.route('/get_filename', methods=['POST'])
def get_filename():
    global filename
    data = request.get_json()
    filename = data.get('filename')

    # Now you can use the 'filename' variable in your Flask code
    print(f"Received filename from localStorage: {filename}")

    # ... Do something with the filename

    return filename

print(filename)

@blueprint.route('/upload_answer', methods=['POST'])
def upload_file():
    try:
        print(1)
        answers_file = request.files['answers']
        if answers_file:
            print(2)
            answers_file.save(f'pictures/{filename}.txt')
            return jsonify({"success": True})
        else:
            print(3)
            return jsonify({"success": False, "error": "No file provided"})
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()  # Import the 'traceback' module at the beginning of your script
        return jsonify({"success": False, "error": str(e)})


@blueprint.route('/next_page')
def next_page():
    return render_template('home/next_page.html')  # Render the result.html template


