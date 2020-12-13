from datetime import datetime

from flask_restful import Resource, reqparse

from components.db import db
from models.user_model import UserModel
from schemas.user_schema import UserSchema


class User(Resource):
    @staticmethod
    def get(id):
        user = UserModel.query.filter_by(id=id).first_or_404(f'No user with id: {id}')

        return {'user': UserSchema().dump(user)}, 200

    @staticmethod
    def put(id):
        user = UserModel.query.filter_by(id=id).first_or_404(f'No user with id: {id}')

        data = parse_users()
        for key, val in data.items():
            setattr(user, key, val)

        db.session.commit()

        return {'user': UserSchema().dump(user)}, 201

    @staticmethod
    def delete(id):
        user = UserModel.query.filter_by(id=id).first_or_404(f'No user with id: {id}')

        db.session.delete(user)
        db.session.commit()

        return {'message': 'user deleted'}, 200


class Users(Resource):
    @staticmethod
    def get():
        users = UserModel.query.all()

        return {'users': UserSchema(many=True).dump(users)}, 200

    @staticmethod
    def post():
        data = parse_users()
        user = UserModel(**data)

        db.session.add(user)
        db.session.commit()

        return {'user': UserSchema().dump(user)}, 201

    def delete(self, id):
        pass


def parse_users():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('surname', type=str, required=True)
    parser.add_argument('login', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('birth_date', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), required=True)
    parser.add_argument('user_type', type=str, required=True)
    return parser.parse_args()
