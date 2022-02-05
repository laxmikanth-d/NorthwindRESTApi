from datetime import datetime
from typing import Dict, Tuple, Union
from flask_restful import Resource, reqparse
from models.Orders import Orders
from flask_jwt_extended import jwt_required

NOT_FOUND = "'{}' not found."


class Order(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("customer_id", type=str, required=False, help="customer_id")

    parser.add_argument("employee_id", type=int, required=False, help="employee_id")

    parser.add_argument("order_date", type=str, required=False, help="order_date")

    parser.add_argument("required_date", type=str, required=False, help="required_date")

    parser.add_argument("shipped_date", type=str, required=False, help="shipped_date")

    parser.add_argument("ship_via", type=int, required=False, help="ship_via")

    parser.add_argument("freight", type=float, required=False, help="freight")

    parser.add_argument("ship_name", type=str, required=False, help="ship_name")

    parser.add_argument("ship_address", type=str, required=False, help="ship_address")

    parser.add_argument("ship_city", type=str, required=False, help="ship_city")

    parser.add_argument("ship_region", type=str, required=False, help="ship_region")

    parser.add_argument(
        "ship_postal_code", type=str, required=False, help="ship_postal_code"
    )

    parser.add_argument("ship_country", type=str, required=False, help="ship_country")

    @jwt_required()
    def get(self, order_id: int) -> Tuple:
        order = Orders.query.filter_by(order_id=order_id).first()

        if order:
            return {"customer_id": order.customer_id}
        else:
            return {"customer_id": NOT_FOUND.format("Customer Id")}

    @jwt_required()
    def put(self, order_id: int) -> Dict:

        data = Order.parser.parse_args()

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
