#!/usr/bin/python
import sys
import logging
import os

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,os.environ.get('APP_PATH'))

from app import create_app
from config import FlaskConfig
application = create_app(FlaskConfig)

application.secret_key = os.getenv('SECRET_KEY')
