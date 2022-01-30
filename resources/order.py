from flask_restful import Resource
from models.Orders import Orders

class Order(Resource):
    
    def get(self, order_id):
        order = Orders.query.filter_by(order_id=10251).first()
        return {'hello': order.customer_id}
        
    