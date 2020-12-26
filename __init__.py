from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


def query_to_dict(ret):
    if ret is not None:
        return jsonify([{key: value for key, value in row.items()} for row in ret if row is not None])
    else:
        return {}


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://g15:{pass}@127.0.0.1/g15'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True

    db = SQLAlchemy(app)

    @app.route('/', methods=['GET'])
    def this_is_library():
        return 'https://www.youtube.com/watch?v=9Wq54dK0aBs&ab_channel=KING5'

    @app.route('/books', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def books():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from books;'))
            return result
        if request.method == 'POST':
            title = request.form.get('title', None)
            author = request.form.get('author', None)
            for_adults = request.form.get('for_adults', None)
            library_branch = request.form.get('library_branch', None)
            category_names = request.form.get('category_names', None)
            db.session.execute(
                f"call add_new_book('{title}', '{author}', {for_adults}, {library_branch}, '{category_names}');")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'PUT':
            id = request.form.get('id', None)
            author = request.form.get('author', None)
            for_adults = request.form.get('for_adults', None)
            title = request.form.get('title', None)
            db.session.execute(
                f"update books set author='{author}', for_adults={for_adults}, title='{title}' where id={id};")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'DELETE':
            id = request.args.get('id', None)
            db.session.execute(f"delete from books where id={id};")
            db.session.commit()
            return {"status": "OK"}

    @app.route('/books/filter', methods=['GET'])
    def book_id():
        id = request.args.get('id', None)
        title = request.args.get('title', None)
        # category = request.args.get('category', None)
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
            # and_specifier = True
        # if category is not None:
        #     if and_specifier:
        #         query += 'and '
        #     query += f'fk_category_id = {category} '
        #     # and_specifier = True
        query += ';'

        result = query_to_dict(db.session.execute(query))
        return result

    @app.route('/availability', methods=['GET'])
    def get_availability():
        title = request.args.get('title', None)
        author = request.args.get('author', None)
        result = query_to_dict(db.session.execute(f"CALL check_availability('{title}', '{author}');"))
        return result

    @app.route('/borrowed', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def borrowed():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from borrowed;'))
            return result
        if request.method == 'POST':
            user_id = request.form.get('user_id', None)
            book_instance_id = request.form.get('book_instance_id', None)
            start_time = request.form.get('start_time', None)
            end_time = request.form.get('end_time', None)
            db.session.execute(
                f"insert into borrowed (user_id, book_instance_id, start_time, end_time) " +
                f"values ({user_id}, {book_instance_id}, '{start_time}', '{end_time}');")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'PUT':
            id = request.form.get('id', None)
            user_id = request.form.get('user_id', None)
            book_instance_id = request.form.get('book_instance_id', None)
            start_time = request.form.get('start_time', None)
            end_time = request.form.get('end_time', None)
            db.session.execute(
                f"update borrowed set user_id={user_id}, book_instance_id={book_instance_id}, " +
                f"start_time='{start_time}', end_time='{end_time}' where id={id};")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'DELETE':
            id = request.args.get('id', None)
            db.session.execute(f"delete from borrowed where id={id};")
            db.session.commit()
            return {"status": "OK"}

    @app.route('/borrowed/user', methods=['GET'])
    def get_borrowed_user():
        login = request.args.get('login', None)
        result = query_to_dict(db.session.execute(f"CALL get_users_books('{login}');"))
        return result

    @app.route('/borrowed/id', methods=['GET'])
    def get_borrowed_id():
        id = request.args.get('id', None)
        result = query_to_dict(db.session.execute(f"select * from borrowed where id={id};"))
        return result

    @app.route('/categories', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def categories():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from categories;'))
            return result
        if request.method == 'POST':
            category_name = request.form.get('category_name', None)
            db.session.execute(
                f"insert into categories (category_name) values ('{category_name}');")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'PUT':
            id = request.form.get('id', None)
            category_name = request.form.get('category_name', None)
            db.session.execute(
                f"update categories set category_name='{category_name}' where id={id};")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'DELETE':
            id = request.args.get('id', None)
            db.session.execute(f"delete from categories where id={id};")
            db.session.commit()
            return {"status": "OK"}

    @app.route('/categories/book', methods=['GET'])
    def get_categories_book():
        title = request.args.get('title', None)
        author = request.args.get('author', None)
        result = query_to_dict(db.session.execute(f"CALL get_category_of_book('{title}', '{author}');"))
        return result

    @app.route('/branches', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def branches():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from library_branches;'))
            return result
        if request.method == 'POST':
            address = request.form.get('address', None)
            library_branch_name = request.form.get('library_branch_name', None)
            db.session.execute(
                f"insert into library_branches (address,library_branch_name) " +
                f"values ('{address}', '{library_branch_name}');")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'PUT':
            id = request.form.get('id', None)
            address = request.form.get('address', None)
            library_branch_name = request.form.get('library_branch_name', None)
            db.session.execute(
                f"update library_branches set address='{address}', library_branch_name='{library_branch_name}'" +
                f" where id={id};")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'DELETE':
            id = request.args.get('id', None)
            db.session.execute(f"delete from library_branches where id={id};")
            db.session.commit()
            return {"status": "OK"}

    @app.route('/branches/id', methods=['GET'])
    def get_branches_id():
        id = request.args.get('id', None)
        result = query_to_dict(db.session.execute(f"select * from library_branches where id={id};"))
        return result

    @app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def get_users():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from users;'))
            return result
        if request.method == 'POST':
            name = request.form.get('name', None)
            surname = request.form.get('surname', None)
            login = request.form.get('login', None)
            password = request.form.get('password', None)
            birth_date = request.form.get('birth_date', None)
            user_type = request.form.get('user_type', None)
            db.session.execute(
                f"insert into users (name,surname,login,password,birth_date,user_type) " +
                f"values ('{name}', '{surname}', '{login}', '{password}', '{birth_date}', '{user_type}');")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'PUT':
            id = request.form.get('id', None)
            name = request.form.get('name', None)
            surname = request.form.get('surname', None)
            login = request.form.get('login', None)
            password = request.form.get('password', None)
            birth_date = request.form.get('birth_date', None)
            user_type = request.form.get('user_type', None)
            db.session.execute(
                f"update users set name='{name}', surname='{surname}', login='{login}', " +
                f"password='{password}', birth_date='{birth_date}', user_type='{user_type}' where id={id};")
            db.session.commit()
            return {"status": "OK"}
        if request.method == 'DELETE':
            id = request.args.get('id', None)
            db.session.execute(f"delete from users where id={id};")
            db.session.commit()
            return {"status": "OK"}

    @app.route('/users/user', methods=['GET'])
    def get_users_user():
        login = request.args.get('login', None)
        result = query_to_dict(db.session.execute(f"select * from users where login='{login}';"))
        return result

    return app
