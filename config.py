import os

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

class FlaskConfig(object):
    SECRET_KEY = os.urandom(24)
    REDIS_URL = os.environ.get('REDIS_URL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URL')\
        if os.environ.get('POSTGRES_URL') != "" and os.environ.get('POSTGRES_URL') is not None  else\
        "postgresql://"+ os.environ.get('DB_USERNAME') +":"+ os.environ.get('DB_PASSWORD')\
        +"@"+ os.environ.get('DB_HOST') +":"+ os.environ.get('DB_PORT') +"/"+os.environ.get('DB_NAME')\
        + os.environ.get('DB_PARAMS')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = dict(pool_size=10)