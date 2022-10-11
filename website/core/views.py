from flask import render_template, request, Blueprint
import os


core = Blueprint('core', __name__)


@core.route("/")
@core.route("/index")
def index():
    return render_template('index.html')





