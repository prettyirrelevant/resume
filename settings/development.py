import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "f99d93d6cd644fddffd80c156996eb42032de525bb2f219b2add23b0167de113"
SQLALCHEMY_DATABASE_URI = "sqlite:///resume.sqlite3"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PDF_PATH = os.path.join(BASE_DIR, "pdfs")
