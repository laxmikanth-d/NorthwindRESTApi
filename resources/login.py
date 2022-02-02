from importlib.resources import Resource
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

class Login(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
    type=str,
    required = True,
    help = 'Username is required.'
    )

    parser.add_argument('password',
    type=str,
    required = True,
    help = 'Password is required.'
    )

    def post(self):
        data = Login.parser.parse_args()

        if data["username"] == data["password"]:
            access_token = create_access_token(data["username"], fresh=True)
            refresh_token = create_refresh_token(data["username"])

            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            },
            200

        return {
            'message': 'Invalid credentials'
        }, 
        401
