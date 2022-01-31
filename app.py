from crypt import methods
from flask import Flask
from flask_restful import Api
from resources.order import Order
from db import db

app = Flask(__name__)

app.config['DEBUG'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/northwind'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lax:password@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'lax'
api = Api(app)

@app.route('/')
def home():
    return '<p>Hello World!!!</p>'

api.add_resource(Order, '/order/<int:order_id>')

if __name__ == '__main__':

    from db import db
    db.init_app(app)

    app.run(port=5000)
