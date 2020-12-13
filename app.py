from flask import Flask
from flask_restful import Api

app = Flask(__name__)
# TODO if running this on your own - change the line below accordingly
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testowy:password@127.0.0.1/books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

from resources.book import Book, Books
from resources.borrowed import Borrowed, Borroweds
from resources.category import Category, Categories
from resources.library_branch import LibraryBranch, LibraryBranches
from resources.user import User, Users

api = Api(app)
api.add_resource(User, '/users/<login>', endpoint='user')
api.add_resource(Users, '/users', endpoint='users')
api.add_resource(Book, '/books/<id>', endpoint='book')
api.add_resource(Books, '/books', endpoint='books')
api.add_resource(LibraryBranch, '/branches/<id>', endpoint='branch')
api.add_resource(LibraryBranches, '/branches', endpoint='branches')
api.add_resource(Category, '/categories/<id>', endpoint='category')
api.add_resource(Categories, '/categories', endpoint='categories')
api.add_resource(Borrowed, '/borrowed/<id>', endpoint='borrowed')
api.add_resource(Borroweds, '/borrowed', endpoint='borroweds')

if __name__ == '__main__':
    app.run()
