from marshmallow import Schema, fields


class RefreshSchema(Schema):
    username = fields.Str()
