from importlib.resources import Resource
from typing import Dict, Tuple
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token


IS_REQUIRED = "'{}' is  required."
INVALID_CREDENTIALS = "Invalid credentials"


class Login(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        "username", type=str, required=True, help=IS_REQUIRED.format("Username")
    )

    parser.add_argument(
        "password", type=str, required=True, help=IS_REQUIRED.format("Password")
    )

    @classmethod
    def post(cls) -> Tuple:
        data = Login.parser.parse_args()

        if data["username"] == data["password"]:
            access_token = create_access_token(data["username"], fresh=True)
            refresh_token = create_refresh_token(data["username"])

            return ({"access_token": access_token, "refresh_token": refresh_token},)
            200

        return ({"message": INVALID_CREDENTIALS},)
        401
