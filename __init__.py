from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.exc import IntegrityError, OperationalError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import re

def query_to_dict(ret):
    if ret is not None:
        return [{key: value for key, value in row.items()} for row in ret if row is not None]
    else:
        return []


def letters_numbers_spaces_special_check(string):
    string = str(string)
    if bool(re.match(r"[a-zA-Z0-9! #$%^&*={}:<>',.ąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]{0,254}", string, re.UNICODE)) and bool(
            re.match(r"^((?!;).)*$", string, re.UNICODE)) and bool(
        re.match(r"^((?!@).)*$", string, re.UNICODE)):
        # re.match(r"^((?!-).)*$", string, re.UNICODE)) and bool(
        return True
    else:
        return False


def letters_numbers_check(string):
    string = str(string)
    if bool(re.match(r"[a-zA-Z0-9]{0,64}", string, re.UNICODE)) and bool(
            re.match(r"^((?!;).)*$", string, re.UNICODE)) and bool(
        re.match(r"^((?!@).)*$", string, re.UNICODE)) and bool(
        re.match(r"^((?!-).)*$", string, re.UNICODE)):
        return True
    else:
        return False


def numbers_check(number):
    number = str(number)
    if bool(re.match(r"[0-9]{0,64}", number, re.UNICODE)) and bool(
            re.match(r"^((?!;).)*$", number, re.UNICODE)) and bool(
        re.match(r"^((?!-).)*$", number, re.UNICODE)) and bool(
        re.match(r"^((?!@).)*$", number, re.UNICODE)):
        return True
    else:
        return False


def date_check(number):
    number = str(number)
    if bool(re.match(r"[1-2][09][0-9][0-9][./-][01][0-9][./-][0123][0-9]", number, re.UNICODE)) and bool(
            re.match(r"^((?!;).)*$", number, re.UNICODE)) and bool(
        re.match(r"^((?!@).)*$", number, re.UNICODE)):
        return True
    else:
        return False


def one_or_zero_check(number):
    number = int(number)
    if number == 1 or number == 0:
        return True
    else:
        return False


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://g15:4fkd9zjj@127.0.0.1/g15'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['JSON_AS_ASCII'] = False

    cors = CORS(app)

    auth = HTTPBasicAuth()
    db = SQLAlchemy(app)

    def delete_by_id(column):
        id_arg = request.args.get('id', None)
        # Regexp
        if not numbers_check(str(id_arg)):
            return {"error": "Wrong input arguments"}, 500
        # Function
        db.session.execute(f"delete from {column} where id={id_arg};")
        db.session.commit()
        return {"status": "OK"}

    @auth.verify_password
    def verify_password(username, password):
        # Regexp check
        if not letters_numbers_check(username):
            return False
        if not letters_numbers_spaces_special_check(password):
            return False
        # Function
        login_and_password = query_to_dict(db.session.execute(
            f"select login, password from users where login='{username}';"))
        if login_and_password:
            if check_password_hash(login_and_password[0]['password'], password):
                return True

    @app.route('/authtest', methods=['GET'])
    @auth.login_required
    def test():
        is_admin = query_to_dict(db.session.execute(
            f"select user_type from users where login='{auth.username()}';"))
        return jsonify(is_admin[0])

    @app.route('/', methods=['GET'])
    def this_is_library():
        return 'https://www.youtube.com/watch?v=9Wq54dK0aBs&ab_channel=KING5'

    @app.route('/books', methods=['GET'])
    def books():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from books;'))
            return jsonify(result)

    @app.route('/book', methods=['POST', 'PUT', 'DELETE'])
    @auth.login_required
    def book():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] != "admin":
            return {"error": "Unauthorized access"}, 401
        if request.method == 'POST':
            title = request.args.get('title', None)
            author = request.args.get('author', None)
            for_adults = request.args.get('for_adults', None)
            library_branch = request.args.get('library_branch', None)
            category_names = request.args.get('category_names', None)
            # Regexp
            if letters_numbers_spaces_special_check(title) is not True or letters_numbers_spaces_special_check(
                    author) is not True or one_or_zero_check(int(for_adults)) is not True or numbers_check(
                str(library_branch)) is not True or letters_numbers_spaces_special_check(category_names) is not True:
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"call add_new_book('{title}', '{author}', {for_adults}, {library_branch}, '{category_names}');")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'PUT':
            id_arg = request.form.get('id', None)
            author = request.form.get('author', None)
            for_adults = request.form.get('for_adults', None)
            title = request.form.get('title', None)
            # Regexp
            if not letters_numbers_spaces_special_check(title) or not letters_numbers_spaces_special_check(
                    author) or not one_or_zero_check(for_adults) or not numbers_check(str(id_arg)):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"update books set author='{author}', for_adults={for_adults}, title='{title}' where id={id_arg};")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
            except OperationalError as e2:
                return {"error": f"{e2.orig}"}, 500
        if request.method == 'DELETE':
            return delete_by_id("books")

    @app.route('/books/filter', methods=['GET'])
    def book_id():
        id_arg = request.args.get('id', None)
        # Regexp
        if not numbers_check(str(id_arg)):
            return {"error": "Wrong input arguments"}, 500
        # Function
        if id_arg is not None:
            query = f'select * from books where id={id_arg};'
        else:
            title = request.args.get('title', 'null')
            if title != 'null':
                title = f"'{title}'"
            cat = request.args.get('category', 'null')
            if cat != 'null':
                cat = f"'{cat}'"
            author = request.args.get('author', 'null')
            if author != 'null':
                author = f"'{author}'"
            # Regexp
            if not letters_numbers_spaces_special_check(title) or not letters_numbers_spaces_special_check(
                    author) or not letters_numbers_spaces_special_check(cat):
                return {"error": "Wrong input arguments"}, 500
            # Function
            query = f"call get_books_filter({title},{author},{cat});"

        result = query_to_dict(db.session.execute(query))
        return jsonify(result)

    @app.route('/availability', methods=['GET'])
    def get_availability():
        title = request.args.get('title', None)
        author = request.args.get('author', None)
        # Regexp
        if not letters_numbers_spaces_special_check(title) or not letters_numbers_spaces_special_check(
                author):
            return {"error": "Wrong input arguments"}, 500
        # Function
        result = query_to_dict(db.session.execute(f"CALL check_availability('{title}', '{author}');"))
        return jsonify(result)

    @app.route('/borroweds', methods=['GET'])
    def borroweds():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from borrowed;'))
            return jsonify(result)

    @app.route('/borrowed', methods=['POST', 'PUT', 'DELETE'])
    @auth.login_required
    def borrowed():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] != "admin":
            return {"error": "Unauthorized access"}, 401
        if request.method == 'POST':
            user_id = request.form.get('user_id', None)
            book_instance_id = request.form.get('book_instance_id', None)
            # Regexp
            if not numbers_check(user_id) or not numbers_check(book_instance_id):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"insert into borrowed (user_id, book_instance_id) " +
                    f"values ({user_id}, {book_instance_id});")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'PUT':
            id_arg = request.form.get('id', None)
            user_id = request.form.get('user_id', None)
            book_instance_id = request.form.get('book_instance_id', None)
            # Regexp
            if not numbers_check(str(id_arg)) or not numbers_check(user_id) or not numbers_check(
                    book_instance_id):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"update borrowed set user_id={user_id}, book_instance_id={book_instance_id}, " +
                    f" where id={id_arg};")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
            except OperationalError:
                return {"error": "Unable to borrow this book, it is probably borrowed already"}, 500
        if request.method == 'DELETE':
            return delete_by_id("borrowed")

    @app.route('/borrowed/user', methods=['GET'])
    @auth.login_required
    def get_borrowed_user():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] == "admin":
            login = request.args.get('login', auth.username())
            # Regexp
            if not letters_numbers_check(login):
                return {"error": "Wrong input arguments"}, 500
            # Function
        else:
            login = auth.username()
        result = query_to_dict(db.session.execute(f"CALL get_users_books('{login}');"))
        return jsonify(result)

    @app.route('/borrowed/id', methods=['GET'])
    @auth.login_required
    def get_borrowed_id():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] != "admin":
            return {"error": "Unauthorized access"}, 401
        id_arg = request.args.get('id', None)
        # Regexp
        if not numbers_check(str(id_arg)):
            return {"error": "Wrong input arguments"}, 500
        # Function
        result = query_to_dict(db.session.execute(f"select * from borrowed where id={id_arg};"))
        return jsonify(result)

    @app.route('/categories', methods=['GET'])
    def categories():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from categories;'))
            return jsonify(result)

    @app.route('/category', methods=['POST', 'PUT', 'DELETE'])
    @auth.login_required
    def category():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] != "admin":
            return {"error": "Unauthorized access"}, 401
        if request.method == 'POST':
            category_name = request.form.get('category_name', None)
            # Regexp
            if not letters_numbers_spaces_special_check(category_name):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"insert into categories (category_name) values ('{category_name}');")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'PUT':
            id_arg = request.form.get('id', None)
            category_name = request.form.get('category_name', None)
            # Regexp
            if not numbers_check(str(id_arg)) or not letters_numbers_spaces_special_check(category_name):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"update categories set category_name='{category_name}' where id={id_arg};")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'DELETE':
            return delete_by_id("categories")

    @app.route('/categories/book', methods=['GET'])
    def get_categories_book():
        title = request.args.get('title', None)
        author = request.args.get('author', None)
        # Regexp
        if not letters_numbers_spaces_special_check(title) or not letters_numbers_spaces_special_check(author):
            return {"error": "Wrong input arguments"}, 500
        # Function
        result = query_to_dict(db.session.execute(f"CALL get_category_of_book('{title}', '{author}');"))
        return jsonify(result)

    @app.route('/branches', methods=['GET'])
    def branches():
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from library_branches;'))
            return jsonify(result)

    @app.route('/branch', methods=['POST', 'PUT', 'DELETE'])
    @auth.login_required
    def branch():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] != "admin":
            return {"error": "Unauthorized access"}, 401
        if request.method == 'POST':
            address = request.form.get('address', None)
            library_branch_name = request.form.get('library_branch_name', None)
            # Regexp
            if not letters_numbers_spaces_special_check(address) or not letters_numbers_spaces_special_check(
                    library_branch_name):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"insert into library_branches (address,library_branch_name) " +
                    f"values ('{address}', '{library_branch_name}');")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'PUT':
            id_arg = request.form.get('id', None)
            address = request.form.get('address', None)
            library_branch_name = request.form.get('library_branch_name', None)
            # Regexp
            if not numbers_check(str(id_arg)) or not letters_numbers_spaces_special_check(
                    address) or not letters_numbers_spaces_special_check(library_branch_name):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"update library_branches set address='{address}', library_branch_name='{library_branch_name}'" +
                    f" where id={id_arg};")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'DELETE':
            return delete_by_id("library_branches")

    @app.route('/branches/id', methods=['GET'])
    def get_branches_id():
        id_arg = request.args.get('id', None)
        # Regexp
        if not numbers_check(str(id_arg)):
            return {"error": "Wrong input arguments"}, 500
        # Function
        result = query_to_dict(db.session.execute(f"select * from library_branches where id={id_arg};"))
        return jsonify(result)

    @app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
    @auth.login_required
    def get_users():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] != "admin":
            return {"error": "Unauthorized access"}, 401
        if request.method == 'GET':
            result = query_to_dict(db.session.execute('select * from users;'))
            return jsonify(result)
        if request.method == 'PUT':
            id_arg = request.form.get('id', None)
            name = request.form.get('name', None)
            surname = request.form.get('surname', None)
            login = request.form.get('login', None)
            password = generate_password_hash(request.form.get('password', None))
            birth_date = request.form.get('birth_date', None)
            user_type = request.form.get('user_type', None)
            # Regexp
            if not numbers_check(str(id_arg)) or not letters_numbers_spaces_special_check(
                    name) or not letters_numbers_spaces_special_check(surname) or not letters_numbers_check(
                login) or not letters_numbers_spaces_special_check(password) or not date_check(
                str(birth_date)) or not letters_numbers_check(user_type):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"update users set name='{name}', surname='{surname}', login='{login}', " +
                    f"password='{password}', birth_date='{birth_date}', user_type='{user_type}' where id={id_arg};")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500
        if request.method == 'DELETE':
            return delete_by_id("users")

    @app.route('/register', methods=['POST'])
    def register():
        if request.method == 'POST':
            name = request.form.get('name', None)
            surname = request.form.get('surname', None)
            login = request.form.get('login', None)
            password = generate_password_hash(request.form.get('password', None))
            birth_date = request.form.get('birth_date', None)
            user_type = request.form.get('user_type', None)
            # Regexp
            if not letters_numbers_spaces_special_check(
                    name) or not letters_numbers_spaces_special_check(surname) or not letters_numbers_check(
                login) or not letters_numbers_spaces_special_check(password) or not date_check(
                str(birth_date)) or not letters_numbers_check(user_type):
                return {"error": "Wrong input arguments"}, 500
            # Function
            try:
                db.session.execute(
                    f"insert into users (name,surname,login,password,birth_date,user_type) " +
                    f"values ('{name}', '{surname}', '{login}', '{password}', '{birth_date}', '{user_type}');")
                db.session.commit()
                return {"status": "OK"}
            except IntegrityError as e:
                return {"error": f"{e.orig}"}, 500

    @app.route('/penalty', methods=['GET'])
    @auth.login_required
    def penalty():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] == "admin":
            login = request.args.get('login', auth.username())
            # Regexp
            if not letters_numbers_check(login):
                return {"error": "Wrong input arguments"}, 500
            # Function
        else:
            login = auth.username()
        result = query_to_dict(db.session.execute(f"call calculate_cash_penalty('{login}');"))
        return {"penalty in PLN": float(result[0]["penalty in PLN"])}, 200

    @app.route('/users/user', methods=['GET'])
    @auth.login_required
    def get_users_user():
        if query_to_dict(db.session.execute(
                f"select user_type from users where login='{auth.username()}';"))[0]["user_type"] == "admin":
            login = request.args.get('login', auth.username())
            # Regexp
            if not letters_numbers_check(login):
                return {"error": "Wrong input arguments"}, 500
            # Function
        else:
            login = auth.username()

        result = query_to_dict(db.session.execute(f"select * from users where login='{login}';"))
        return jsonify(result)

    return app
