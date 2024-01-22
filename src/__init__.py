from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config
from .middlewares.response import init_app

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    
    # Enable CORS for all routes
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    init_app(app)

    return app
