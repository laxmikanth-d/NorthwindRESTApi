from marshmallow import Schema, fields


class LoginSchema(Schema):
    username = fields.Str()
    password = fields.Str()
