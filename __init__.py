from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


def query_to_dict(ret):
    if ret is not None:
        return jsonify([{key: value for key, value in row.items()} for row in ret if row is not None])
    else:
        return {}


def create_app():
    app = Flask(__name__)
    # TODO if running this on your own - change the line below accordingly
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testowy:password@127.0.0.1/books'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://g15:4fkd9zjj@127.0.0.1/g15'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True

    db = SQLAlchemy(app)

    @app.route('/')
    def this_is_library():
        return 'https://www.youtube.com/watch?v=9Wq54dK0aBs&ab_channel=KING5'

    @app.route('/books')
    def get_books():
        result = query_to_dict(db.session.execute('select * from books;'))
        return result

    @app.route('/books/filter')
    def get_book_id():
        id = request.args.get('id', None)
        title = request.args.get('title', None)
        category = request.args.get('category', None)
        author = request.args.get('author', None)

        query = 'select * from books where '
        and_specifier = False

        if id is not None:
            query += f'id={id} '
            and_specifier = True

        if title is not None:
            if and_specifier:
                query += 'and '
            filtered = "'%%" + title + "%%'"
            query += f'title like {filtered} '
            and_specifier = True

        if author is not None:
            if and_specifier:
                query += 'and '
            filtered = "'%%" + author + "%%'"
            query += f'author like {filtered} '
            and_specifier = True

        if category is not None:
            if and_specifier:
                query += 'and '
            query += f'fk_category_id = {category} '
            and_specifier = True

        query += ';'

        result = query_to_dict(db.session.execute(query))
        return result

    @app.route('/availability')
    def get_availability():
        title = request.args.get('title', None)
        author = request.args.get('author', None)
        result = query_to_dict(db.session.execute(f"CALL check_availability('{title}', '{author}');"))
        return result

    @app.route('/borrowed')
    def get_borrowed():
        result = query_to_dict(db.session.execute('select * from borrowed;'))
        return result

    @app.route('/borrowed/user')
    def get_borrowed_user():
        login = request.args.get('login', None)
        result = query_to_dict(db.session.execute(f"CALL get_users_books('{login}');"))
        return result

    @app.route('/borrowed/id')
    def get_borrowed_id():
        id = request.args.get('id', None)
        result = query_to_dict(db.session.execute(f"select * from borrowed where id={id};"))
        return result

    @app.route('/categories')
    def get_categories():
        result = query_to_dict(db.session.execute('select * from categories;'))
        return result

    @app.route('/categories/book')
    def get_categories_book():
        title = request.args.get('title', None)
        author = request.args.get('author', None)
        result = query_to_dict(db.session.execute(f"CALL get_category_of_book('{title}', '{author}');"))
        return result

    @app.route('/branches')
    def get_branches():
        result = query_to_dict(db.session.execute('select * from library_branches;'))
        return result

    @app.route('/branches/id')
    def get_branches_id():
        id = request.args.get('id', None)
        result = query_to_dict(db.session.execute(f"select * from library_branches where id={id};"))
        return result

    @app.route('/users')
    def get_users():
        result = query_to_dict(db.session.execute('select * from users;'))
        return result

    @app.route('/users/user')
    def get_users_user():
        login = request.args.get('login', None)
        result = query_to_dict(db.session.execute(f"select * from users where login='{login}';"))
        return result

    return app
