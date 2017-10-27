import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()


class BaseMixin(object):

    @declared_attr
    def id(cls):

        return db.Column(db.Integer, primary_key=True)

    @declared_attr
    def created_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @declared_attr
    def updated_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)


from .user import *
