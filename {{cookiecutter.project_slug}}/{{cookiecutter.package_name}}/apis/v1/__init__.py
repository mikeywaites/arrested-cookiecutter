from arrested import ArrestedAPI
from .users import users_resource
from .middleware import basic_auth

api_v1 = ArrestedAPI(url_prefix='/v1', before_all_hooks=[basic_auth])
api_v1.register_resource(users_resource, defer=True)
