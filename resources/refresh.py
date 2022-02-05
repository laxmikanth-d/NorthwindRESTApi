from typing import Dict
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    create_access_token
)

class Refresh(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
    type=str,
    required = True)

    @jwt_required(refresh=True)
    def post(self) -> Dict:
        data = Refresh.parser.parse_args()
        access_token = create_access_token(data['username'])
        return jsonify(access_token=access_token)
