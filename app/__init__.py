from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    bootstrap.init_app(app)

    app.config.from_object(config_options[config_name])

    return app