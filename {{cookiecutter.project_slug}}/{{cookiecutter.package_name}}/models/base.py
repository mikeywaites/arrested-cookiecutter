import datetime

from sqlalchemy.ext.declarative import declared_attr

from . import db


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
