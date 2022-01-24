from flask import Flask
from flask_restful import Api
from resources.order import Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/northwind'

api = Api(app)

@app.route('/')
def home():
    return '<p>Hello World!!!</p>'

api.add_resource(Order, '/order/')
# api.add_resource(Order, '/order/<int:order_id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
