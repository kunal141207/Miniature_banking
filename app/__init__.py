from config import FlaskConfig
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_gzip import Gzip

from redis.client import Redis

from app.models import User
import redis


db = SQLAlchemy()

redis_db = Redis.from_url(url=FlaskConfig.REDIS_URL)

migrate = Migrate()
login = LoginManager()
login.login_view = "authorization.sign_in"


def create_app(config_class=FlaskConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.devices import bp as devices_bp
    app.register_blueprint(devices_bp)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    Gzip(app)

    return app
