from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin, DBObjectMixin

from {{ cookiecutter.package_name }}.models import db, User
from .mappers import UserMapper

users_resource = Resource('users', __name__, url_prefix='/users')


class UsersIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):

    name = 'list'
    many = True
    mapper_class = UserMapper
    model = User

    def get_query(self):

        stmt = db.session.query(User)
        return stmt


class UserObjectEndpoint(KimEndpoint, DBObjectMixin):

    name = 'object'
    mapper_class = UserMapper
    model = User

    def get_query(self):

        stmt = db.session.query(User)
        return stmt


users_resource.add_endpoint(UsersIndexEndpoint)
users_resource.add_endpoint(UserObjectEndpoint)
