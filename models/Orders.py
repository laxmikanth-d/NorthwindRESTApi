from db import db

class Orders(db.Model):
    __tablename__ = 'orders'

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

    # def __repr__(self) -> str:
    #     return f'{self.order_id} -> {self.employee_id} -> {self.ship_name}'

    def json(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'employee_id': self.employee_id,
            'order_date': str(self.order_date),
            'required_date': str(self.required_date),
            'shipped_date': str(self.shipped_date),
            'ship_via': self.ship_via,
            'freight': self.freight,
            'ship_name': self.ship_name,
            'ship_address': self.ship_address,
            'ship_city': self.ship_city,
            'ship_region': self.ship_region,
            'ship_postal_code': self.ship_postal_code,
            'ship_country': self.ship_country            
        }

    @classmethod
    def find_by_orderid(cls, order_id):
        return cls.query.filter_by(order_id = order_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
