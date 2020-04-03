from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

assets = Environment(app)
assets.register('css',
                Bundle('less/base.less',
                       output='css/style.css'))
assets.register('js', Bundle(
    'js/account.js',
    filters='jsmin',
    output='gen/script.js'))


login = LoginManager(app)
login.login_view = 'login'
login.login_message = "Пожалуйста, войдите, чтобы открыть эту страницу."

db = SQLAlchemy(app)

