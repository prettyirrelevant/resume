from os import environ
from .development import *

DEBUG = False
ENV = "production"
SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
SECRET_KEY = environ.get("SECRET_KEY")
