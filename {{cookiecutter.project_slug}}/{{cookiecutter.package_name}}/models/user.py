from sqlalchemy_utils import EmailType, PasswordType
from .base import db, BaseMixin


class User(BaseMixin, db.Model):

    __tablename__ = 'users'

    name = db.Column(db.Unicode(255), nullable=False)
    email = db.Column(EmailType, nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
        ],
    ))
