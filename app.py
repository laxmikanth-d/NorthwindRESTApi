from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.login import Login
from resources.order import Order
from resources.refresh import Refresh

app = Flask(__name__)

app.config["DEBUG"] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/northwind'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lax:password@localhost/northwind"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=10)

app.secret_key = "lax"
api = Api(app)

jwt = JWTManager(app)


@app.route("/")
def home():
    return "<p>Hello World!!!</p>"


api.add_resource(Order, "/order/<int:order_id>")
api.add_resource(Login, "/login/")
api.add_resource(Refresh, "/refresh/")

if __name__ == "__main__":

    from db import db

    db.init_app(app)

    app.run(port=5000)
