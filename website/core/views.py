from flask import render_template, request, Blueprint
import os


core = Blueprint('core', __name__)


@core.route("/", methods=["GET", "POST"])
@core.route("/index", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        image_link = request.form.get("image-link")

        # Do OCR Shits
        text_result=image_link

        return render_template('search.html', text_result=text_result)


    return render_template('index.html')





