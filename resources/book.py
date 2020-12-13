from flask_restful import Resource, reqparse

from components.db import db
from models.book_model import BookModel
from schemas.book_schema import BookSchema


class Book(Resource):
    @staticmethod
    def get(id):
        book = BookModel.query.filter_by(id=id).first_or_404(f'No book with id: {id}')

        return {'book': BookSchema().dump(book)}, 200

    @staticmethod
    def put(id):
        book = BookModel.query.filter_by(id=id).first_or_404(f'No book with id: {id}')

        data = parse_books()
        for key, val in data.items():
            setattr(book, key, val)

        db.session.commit()

        return {'book': BookSchema().dump(book)}, 201

    @staticmethod
    def delete(id):
        book = BookModel.query.filter_by(id=id).first_or_404(f'No book with id: {id}')

        db.session.delete(book)
        db.session.commit()

        return {'message': 'book deleted'}, 200


class Books(Resource):
    @staticmethod
    def get():
        books = BookModel.query.all()

        return {'books': BookSchema(many=True).dump(books)}, 200

    @staticmethod
    def post():
        data = parse_books()
        book = BookModel(**data)

        db.session.add(book)
        db.session.commit()

        return {'book': BookSchema().dump(book)}, 201

    def delete(self, id):
        pass


def parse_books():
    parser = reqparse.RequestParser()
    parser.add_argument('fk_branch_id', type=int, required=True)
    parser.add_argument('fk_category_id', type=int, required=True)
    parser.add_argument('author', type=str, required=True)
    parser.add_argument('for_adults', type=int, required=True)
    parser.add_argument('title', type=str, required=True)
    return parser.parse_args()
