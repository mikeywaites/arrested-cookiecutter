from kim import field

from .base import BaseMapper

from {{ cookiecutter.package_name }}.models import Character


class CharacterMapper(BaseMapper):

    __type__ = Character

    name = field.String()
