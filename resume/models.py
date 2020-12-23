from sqlalchemy import func

from . import db


class Download(db.Model):
    __tablename__ = "downloads"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
