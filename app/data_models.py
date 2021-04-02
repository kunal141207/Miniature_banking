from app import db
from sqlalchemy import inspect
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column("user_id", db.String(128), primary_key=True)
    user_name = db.Column(db.String(34), unique=True)
    password_hash = db.Column(db.String(128))

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<User: " + self.user_name + ">"