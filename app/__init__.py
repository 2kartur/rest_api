from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        # if os.environ.get('DATABASE_URL') is None: # for local work
        #     app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///form.db', SECRET_KEY = 'asfdsfsaaffdf')
        # else: # for heroku work
        #     app.config.from_object('config')
        # print(os.environ.get('DATABASE_URL'))
        db.init_app(app)

        from .api import api_bp
        #from .swagger import swagger_bp

        app.register_blueprint(api_bp, url_prefix='/api')
        #app.register_blueprint(swagger_bp, url_prefix='/swagger')


    return app