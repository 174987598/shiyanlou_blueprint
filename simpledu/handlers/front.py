from flask import Blueprint
from simpledu.models import Course
from flask import render_template

front =Blueprint('front',__name__,url_prefix='/')

@front.route('/')
def index():
    courses =Course.query.all()
    return render_template('index.html',courses=courses)


