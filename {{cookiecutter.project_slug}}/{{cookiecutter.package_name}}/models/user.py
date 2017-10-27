from sqlalchemy_utils import EmailType, PasswordType
from .base import db, BaseMixin


__all__ = ['User']


class User(BaseMixin, db.Model):

    __tablename__ = '{{cookiecutter.package_name}}_user'

    name = db.Column(db.Unicode(255), nullable=False)
    email = db.Column(EmailType, nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
        ],
    ))
