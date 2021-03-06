from typing import Dict

from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource

from schemas import refresh


class Refresh(Resource):
    @classmethod
    @jwt_required(refresh=True)
    def post(cls) -> Dict:

        refresh_schema = refresh.RefreshSchema()

        data = refresh_schema.load(request.get_json())

        data = Refresh.parser.parse_args()
        access_token = create_access_token(data["username"])
        return jsonify(access_token=access_token)
