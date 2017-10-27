from flask import Flask
from flask_alembic import Alembic

from {{ cookiecutter.package_name }}.models import db
from {{ cookiecutter.package_name }}.apis import api_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object('{{ cookiecutter.package_name}}.config.settings')

    db.init_app(app)
    api_v1.init_app(app)
    Alembic(app)

    return app
