from kim import field, role

from .base import BaseMapper

from {{ cookiecutter.package_name }}.models import User


class UserMapper(BaseMapper):

    __type__ = User

    name = field.String()
    email = field.String()

    __roles__ = {
        '__default__': role.blacklist('password')
    }
