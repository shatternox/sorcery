import os
import datetime
from flask import Flask
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = "3be535d9d3c71344b173553b0134412b"


from website.core.views import core

app.register_blueprint(core)




