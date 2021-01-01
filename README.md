# Library API for Databases Project AGH

## GET

#### GET / 
Gets you a classic youtube video.

#### GET /authtest
Basic authentication:
* login
* password

Gets you a "success" if auth was handled correctly.

#### GET /books 
Gets you all the books.

#### GET /books/filter
Parameters:
* id (int)
* title (str)
* author (str)
* category (str)

Example usage:
* /books/filter?id=1

Gets you only the books with "cip" in the title and "pa" in the author's name.

#### GET /availability
Parameters:
* title (str)
* author (str)

Example usage:
* /availability?title=Solaris&author=Stanislaw%20Lem

Gets you the availability of Stanisław Lem's "Solaris"

#### GET /borroweds
Gets you all the borrowed books.

#### GET /borrowed/user
Basic authentication:
* login
* password

Parameters:
* login (str)

Example usage:
* /borrowed/user?login=achudy"

Gets you all books borrowed by the user with login "achudy". If not admin, will only see info about himself.

#### GET /borrowed/id
Basic authentication:
* login
* password

Parameters:
* id (int)

Example usage:
* /borrowed/id?id=1 

Gets you the borrowed book with an id=1

#### GET /categories 
Gets you all the categories of books.

#### GET /categories/book
Parameters:
* title (str)
* author (str)

Example usage:
* /categories/book?title=Cos%20sie%20konczy,%20cos%20sie%20zaczyna&author=Andrzej%20Sapkowski

Gets you the category of Andrzej Sapkowski's "C.s.k.c.s.z."

#### GET /branches 
Gets you all the library branches.

#### GET /branches/id
Parameters:
* id (int)

Example usage:
* /branches/id?id=1 

Gets you only the branch with id=1.

#### GET /users 
Basic authentication:
* login
* password

Gets you all the users.

#### GET /users/user
Basic authentication:
* login
* password

Parameters:
* login (str)

Example usage:
* /users/user?login=achudy

Gets you only the user with login "achudy". If not admin, will only see info about himself.

#### GET /penalty
Basic authentication:
* login
* password

Parameters: 
* login (str)

Gets you a penalty for a user. If not admin, will only see info about himself.


## POST

#### POST /register

Form data: 
* name (str)
* surname (str)
* login (str)
* password (str)
* birth_date (date)
* user_type (str)

Registers a user.

#### POST /book
Basic authentication:
* login
* password

Form data: 
* title (str)
* author (str)
* for_adults (int)
* library_branch (int)
* category_names (str) 

Posts a book.

#### POST /borrowed
Basic authentication:
* login
* password

Form data: 
* user_id (int)
* book_instance_id (int)
* start_time (date e.g. 2021-06-09)
* end_time (date)

Posts a borrowed record.

#### POST /category
Basic authentication:
* login
* password

Form data: 
* category_name (str)

Posts a category.

#### POST /branch
Basic authentication:
* login
* password

Form data: 
* address (str)
* library_branch_name (str)

Posts a library branch.


## PUT

#### PUT /book
Basic authentication:
* login
* password

Form data: 
* id (int)
* author (str)
* for_adults (str)
* title (int)

Updates a book.

#### PUT /borrowed
Basic authentication:
* login
* password

Form data: 
* id (int)
* user_id (int)
* book_instance_id (int)
* start_time (date e.g. 2021-06-09)
* end_time (date)

Updates a borrowed record.

#### PUT /category
Basic authentication:
* login
* password

Form data: 
* id (int)
* category_name (str)

Updates a category.

#### PUT /branch
Basic authentication:
* login
* password

Form data: 
* id (int)
* address (str)
* library_branch_name (str)

Updates a library branch.

#### PUT /users
Basic authentication:
* login
* password

Form data: 
* id (int)
* name (str)
* surname (str)
* login (str)
* password (str)
* birth_date (date)
* user_type (str)

Updates a user.

## DELETE

#### DELETE /book
Basic authentication:
* login
* password

Parameters:
* id (int)

Example usage:
* /books?id=1

Deletes a book.

#### DELETE /borrowed
Basic authentication:
* login
* password

Parameters:
* id (int)

Deletes a borrowed record.

#### DELETE /category
Basic authentication:
* login
* password

Parameters:
* id (int)

Deletes a category.

#### DELETE /branch
Basic authentication:
* login
* password

Parameters:
* id (int)

Deletes a library branch.

#### DELETE /users
Basic authentication:
* login
* password

Parameters:
* id (int)

Deletes a user.

