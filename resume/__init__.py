from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(development, production):
    app = Flask(__name__)
    app.config.from_object(development)
    app.config.from_object(production)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes

        return app
