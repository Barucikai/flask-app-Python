from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app) #Incializa Bootstrap en Flask
    #Creacion de Index
    app.config.from_object(Config)
    app.register_blueprint(auth)

    return app
