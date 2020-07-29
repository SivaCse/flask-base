import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


from config import BaseConfig

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
database_file = "sqlite:///{}".format(os.path.join(APP_ROOT, "sampledb.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

def create_app(environment):

    env = os.getenv("ENV")

    app.config.from_object(environment.get(env))

    from .api.user import user
    from .api.post import post


    """ Cors settings will be here. We maybe use this endpoint later. """
    cors = CORS(app, resources={
        r'/api/*': {
            'origins': BaseConfig.ORIGINS
        }
    })


    app.url_map.strict_slashes = False


    app.register_blueprint(user, url_prefix='/api/users')
    app.register_blueprint(post, url_prefix='/api/post')


    return app
