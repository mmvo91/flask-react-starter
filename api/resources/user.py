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
        data = request.json
        username = data['username']
        password = data['password']

        current = models.User.query.filter_by(username=username).first()
        if current is not None:
            return {'msg': f'Username {current.username} is already taken. Please try another name'}
        else:
            hashed = bcrypt.generate_password_hash(password)
            new = User(
                username=username,
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
        data = request.json
        username = data['username']
        password = data['password']

        current = models.User.query.filter_by(username=username).first()
        if current is not None:
            if not current.active:
                return {'msg': "Account not activated. Please contact administrator to activate."}
        else:
            return {'msg': "Wrong credentials"}

        if bcrypt.check_password_hash(current.password, password):
            access_token = create_access_token(identity=current.id)
            refresh_token = create_refresh_token(identity=current.id)

            current.last_login = datetime.datetime.now()

            response = {
                'id': current.id,
                'msg': f"Logged in as {current.username}",
            }

            response = jsonify(response)

            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)

            sql.session.commit()

            return response
        else:
            return {'msg': 'Wrong credentials'}
