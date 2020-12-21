from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_envvar("FLASK_SETTINGS", silent=True)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        return app
