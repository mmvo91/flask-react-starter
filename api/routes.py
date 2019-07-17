from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from api import resources

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
cors = CORS(api_bp, supports_credentials=True)

api.add_resource(resources.User, "/user")
