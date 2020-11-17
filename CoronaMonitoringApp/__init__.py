from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from . import models
    
    db.init_app(app)
    migrate.init_app(app, db)    
    
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app