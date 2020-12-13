from flask_restful import Resource, reqparse

from components.db import db
from models.library_branch_model import LibraryBranchModel
from schemas.library_branch_schema import LibraryBranchSchema


class LibraryBranch(Resource):
    @staticmethod
    def get(id):
        library_branch = LibraryBranchModel.query.filter_by(id=id).first_or_404(f'No branch with id: {id}')

        return {'library_branch': LibraryBranchSchema().dump(library_branch)}, 200

    @staticmethod
    def put(id):
        library_branch = LibraryBranchModel.query.filter_by(id=id).first_or_404(f'No branch with id: {id}')

        data = parse_branches()
        for key, val in data.items():
            setattr(library_branch, key, val)

        db.session.commit()

        return {'library_branch': LibraryBranchSchema().dump(library_branch)}, 201

    @staticmethod
    def delete(id):
        library_branch = LibraryBranchModel.query.filter_by(id=id).first_or_404(f'No branch with id: {id}')

        db.session.delete(library_branch)
        db.session.commit()

        return {'message': 'branch deleted'}, 200


class LibraryBranches(Resource):
    @staticmethod
    def get():
        library_branches = LibraryBranchModel.query.all()

        return {'library_branches': LibraryBranchSchema(many=True).dump(library_branches)}, 200

    @staticmethod
    def post():
        data = parse_branches()
        library_branch = LibraryBranchModel(**data)

        db.session.add(library_branch)
        db.session.commit()

        return {'library_branch': LibraryBranchSchema().dump(library_branch)}, 201

    def delete(self):
        pass


def parse_branches():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('address', type=str, required=True)
    return parser.parse_args()
