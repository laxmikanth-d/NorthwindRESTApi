from db import db
from typing import Dict, Union
from datetime import date

OrdersJson = Dict[str, Union[int, str, float]]


class Orders(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    customer_id = db.Column(db.String(15), nullable=True)
    employee_id = db.Column(db.Integer, nullable=True)
    order_date = db.Column(db.Date, nullable=True)
    required_date = db.Column(db.Date, nullable=True)
    shipped_date = db.Column(db.Date, nullable=True)
    ship_via = db.Column(db.Integer, nullable=True)
    freight = db.Column(db.Float, nullable=True)
    ship_name = db.Column(db.String(40), nullable=True)
    ship_address = db.Column(db.String(60), nullable=True)
    ship_city = db.Column(db.String(15), nullable=True)
    ship_region = db.Column(db.String(15), nullable=True)
    ship_postal_code = db.Column(db.String(10), nullable=True)
    ship_country = db.Column(db.String(15), nullable=True)

    def __init__(
        self,
        order_id: int,
        customer_id: str,
        employee_id: int,
        order_date: date,
        required_date: date,
        shipped_date: date,
        ship_via: int,
        freight: float,
        ship_name: str,
        ship_address: str,
        ship_city: str,
        ship_region: str,
        ship_postal_code: str,
        ship_country: str,
    ) -> None:
        self.order_id = (order_id,)
        self.customer_id = (customer_id,)
        self.employee_id = (employee_id,)
        self.order_date = (order_date,)
        self.required_date = (required_date,)
        self.shipped_date = (shipped_date,)
        self.ship_via = (ship_via,)
        self.freight = (freight,)
        self.ship_name = (ship_name,)
        self.ship_address = (ship_address,)
        self.ship_city = (ship_city,)
        self.ship_region = (ship_region,)
        self.ship_postal_code = (ship_postal_code,)
        self.ship_country = ship_country

    # def __repr__(self) -> str:
    #     return f'{self.order_id} -> {self.employee_id} -> {self.ship_name}'

    def json(self) -> OrdersJson:
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "employee_id": self.employee_id,
            "order_date": str(self.order_date),
            "required_date": str(self.required_date),
            "shipped_date": str(self.shipped_date),
            "ship_via": self.ship_via,
            "freight": self.freight,
            "ship_name": self.ship_name,
            "ship_address": self.ship_address,
            "ship_city": self.ship_city,
            "ship_region": self.ship_region,
            "ship_postal_code": self.ship_postal_code,
            "ship_country": self.ship_country,
        }

    # Make sure the "Orders" in return is in double quotes.
    # Because Orders definition is not available yet for Python interpretor.
    # If you have to return list of Orders just hint it as List["Orders"]
    @classmethod
    def find_by_orderid(cls, order_id: int) -> "Orders":
        return cls.query.filter_by(order_id=order_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
