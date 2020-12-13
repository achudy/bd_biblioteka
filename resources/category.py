from flask_restful import Resource, reqparse

from components.db import db
from models.category_model import CategoryModel
from schemas.category_schema import CategorySchema


class Category(Resource):
    @staticmethod
    def get(id):
        category = CategoryModel.query.filter_by(id=id).first_or_404(f'No category with id: {id}')

        return {'category': CategorySchema().dump(category)}, 200

    @staticmethod
    def put(id):
        category = CategoryModel.query.filter_by(id=id).first_or_404(f'No category with id: {id}')

        data = parse_categories()
        for key, val in data.items():
            setattr(category, key, val)

        db.session.commit()

        return {'category': CategorySchema().dump(category)}, 201

    @staticmethod
    def delete(id):
        category = CategoryModel.query.filter_by(id=id).first_or_404(f'No category with id: {id}')

        db.session.delete(category)
        db.session.commit()

        return {'message': 'category deleted'}, 200


class Categories(Resource):
    @staticmethod
    def get():
        categories = CategoryModel.query.all()

        return {'categories': CategorySchema(many=True).dump(categories)}, 200

    @staticmethod
    def post():
        data = parse_categories()
        category = CategoryModel(**data)

        db.session.add(category)
        db.session.commit()

        return {'category': CategorySchema().dump(category)}, 201

    def delete(self, id):
        pass


def parse_categories():
    parser = reqparse.RequestParser()
    parser.add_argument('category_name', type=str, required=True)
    return parser.parse_args()
