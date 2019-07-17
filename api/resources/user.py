import datetime

from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
)

from api import schemas, models
from api.extensions import bcrypt, sql


class Users(Resource):
    def post(self):
        data = request.get_json()['user']

        current = User.query.filter_by(username=data['username']).first()
        if current is not None:
            return {'msg': f'Username {current.username} is already taken. Please try another name'}
        else:
            hashed = bcrypt.generate_password_hash(data['password'])
            new = User(
                username=data['username'],
                password=hashed.decode('utf-8'),
                email=data['email']
            )

            sql.session.add(new)
            sql.session.commit()

            return {'msg': 'User Created'}


class User(Resource):
    @jwt_required
    def get(self, user_id):
        user = models.User.query.get(user_id)
        schema = schemas.User()

        return schema.dump(user)

    def post(self):
        data = request.get_json()['user']

        current = User.query.filter_by(username=data['username']).first()
        if current is not None:
            if not current.active:
                return {'message': "Account not activated. Please contact administrator to activate."}
        else:
            return {'message': "Wrong credentials"}

        if bcrypt.check_password_hash(current.password, data['password']):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])

            current.last_login = datetime.datetime.now()

            response = {
                'message': f"Logged in as {current.username}",
                'access_token': f'{access_token}',
                'refresh_token': f'{refresh_token}'
            }

            response = jsonify(response)

            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)

            sql.session.commit()

            return response
        else:
            return {'message': 'Wrong credentials'}
