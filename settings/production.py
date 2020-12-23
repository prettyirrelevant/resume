from os import environ
from .development import *

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SECRET_KEY = environ.get('SECRET_KEY')