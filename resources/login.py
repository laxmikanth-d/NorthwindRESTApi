from typing import Tuple

from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from marshmallow import ValidationError

from schemas import login

IS_REQUIRED = "'{}' is  required."
INVALID_CREDENTIALS = "Invalid credentials"


class Login(Resource):
    @classmethod
    def post(cls) -> Tuple:
        login_schema = login.LoginSchema()

        try:
            data = login_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if data["username"] == data["password"]:
            access_token = create_access_token(data["username"], fresh=True)
            refresh_token = create_refresh_token(data["username"])

            return ({"access_token": access_token, "refresh_token": refresh_token},)
            200

        return ({"message": INVALID_CREDENTIALS},)
        401
