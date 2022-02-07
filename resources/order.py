from datetime import datetime
from typing import Tuple
from schemas.orders import OrdersSchema
from flask_restful import Resource
from models.Orders import Orders, OrdersJson
from flask_jwt_extended import jwt_required
from flask import request
from marshmallow import ValidationError

NOT_FOUND = "'{}' not found."


class Order(Resource):
    @classmethod
    @jwt_required()
    def get(cls, order_id: int) -> Tuple:
        order = Orders.query.filter_by(order_id=order_id).first()

        if order:
            return {"customer_id": order.customer_id}
        else:
            return {"customer_id": NOT_FOUND.format("Customer Id")}

    @classmethod
    @jwt_required()
    def put(cls, order_id: int) -> OrdersJson:
        orders_schema = OrdersSchema()

        try:
            data = orders_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        order = Orders.find_by_orderid(order_id)

        if order is None:
            order = Orders(order_id, **data)
        else:
            if data["customer_id"]:
                order.customer_id = data["customer_id"]
            if data["employee_id"]:
                order.employee_id = data["employee_id"]
            if data["order_date"]:
                order.order_date = datetime.strptime(data["order_date"], "%Y-%m-%d")
            if data["required_date"]:
                order.required_date = datetime.strptime(
                    data["required_date"], "%Y-%m-%d"
                )
            if data["shipped_date"]:
                order.shipped_date = datetime.strptime(data["shipped_date"], "%Y-%m-%d")
            if data["ship_via"]:
                order.ship_via = data["ship_via"]
            if data["freight"]:
                order.freight = data["freight"]
            if data["ship_name"]:
                order.ship_name = data["ship_name"]
            if data["ship_address"]:
                order.ship_address = data["ship_address"]
            if data["ship_city"]:
                order.ship_city = data["ship_city"]
            if data["ship_region"]:
                order.ship_region = data["ship_region"]
            if data["ship_postal_code"]:
                order.ship_postal_code = data["ship_postal_code"]
            if data["ship_country"]:
                order.ship_country = data["ship_country"]

        order.save_to_db()

        return order.json()
