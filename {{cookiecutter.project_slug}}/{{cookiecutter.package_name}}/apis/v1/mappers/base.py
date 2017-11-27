from kim import Mapper, field


class BaseMapper(Mapper):

    id = field.Integer(read_only=True)
    created_at = field.DateTime(read_only=True)
    updated_at = field.DateTime(read_only=True)
