from flask import Flask
from flask_restful import Api
from resources.order import Order
from db import db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/northwind'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lax:Par$w0RD@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

@app.route('/')
def home():
    return '<p>Hello World!!!</p>'

api.add_resource(Order, '/order/<string:order_id>')
# api.add_resource(Order, '/order/<int:order_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
