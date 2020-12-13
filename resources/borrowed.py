from datetime import datetime

from flask_restful import Resource, reqparse

from components.db import db
from models.borrowed_model import BorrowedModel
from schemas.borrowed_schema import BorrowedSchema


class Borrowed(Resource):
    @staticmethod
    def get(id):
        borrowed = BorrowedModel.query.filter_by(id=id).first_or_404(f'Nothing borrowed with id: {id}')

        return {'borrowed': BorrowedSchema().dump(borrowed)}, 200

    @staticmethod
    def put(id):
        borrowed = BorrowedModel.query.filter_by(id=id).first_or_404(f'Nothing borrowed with id: {id}')

        data = parse_borrowed()
        for key, val in data.items():
            setattr(borrowed, key, val)

        db.session.commit()

        return {'borrowed': BorrowedSchema().dump(borrowed)}, 201

    @staticmethod
    def delete(id):
        borrowed = BorrowedModel.query.filter_by(id=id).first_or_404(f'Nothing borrowed with id: {id}')

        db.session.delete(borrowed)
        db.session.commit()

        return {'message': 'borrow deleted'}, 200


class Borroweds(Resource):
    @staticmethod
    def get():
        borroweds = BorrowedModel.query.all()

        return {'borroweds': BorrowedSchema(many=True).dump(borroweds)}, 200

    @staticmethod
    def post():
        data = parse_borrowed()
        borrowed = BorrowedModel(**data)

        db.session.add(borrowed)
        db.session.commit()

        return {'borrowed': BorrowedSchema().dump(borrowed)}, 201

    def delete(self, id):
        pass


def parse_borrowed():
    parser = reqparse.RequestParser()
    parser.add_argument('fk_book_id', type=int, required=True)
    parser.add_argument('fk_user_id', type=int, required=True)
    parser.add_argument('start_time', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), required=True)
    parser.add_argument('end_time', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), required=True)
    return parser.parse_args()
