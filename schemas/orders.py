from marshmallow import Schema, fields

class OrdersSchema(Schema):
    order_id = fields.Int()
    customer_id = fields.Str(required=True)
    employee_id = fields.Int()
    order_date = fields.Str()
    required_date = fields.Str()
    shipped_date = fields.Str()
    ship_via = fields.Int()
    freight = fields.Float()
    ship_name = fields.Str()
    ship_address = fields.Str()
    ship_city = fields.Str()
    ship_region = fields.Str()
    ship_postal_code = fields.Str()
    ship_country = fields.Str()