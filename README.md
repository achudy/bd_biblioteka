# Library API for Databases Project AGH

## GET

#### GET / 
Gets you a classic youtube video.

#### GET /books 
Gets you all the books.

#### GET /books/filter
Parameters:
* id (int)
* title (str)
* author (str)

Example usage:
* /books/filter?title=ci&author=pa

Gets you only the books with "cip" in the title and "pa" in author's name.

#### GET /availability
Parameters:
* title (str)
* author (str)

Example usage:
* /availability?title=Solaris&author=Stanisław%20Lem

Gets you the availability of Stanisław Lem's "Solaris"

#### GET /borrowed 
Gets you all the borrowed books.

#### GET /borrowed/user
Parameters:
* login (str)

Example usage:
* /borrowed/user?login=achudy 

Gets you all books borrowed by the user with login "achudy"

#### GET /borrowed/id
Parameters:
* id (int)

Example usage:
* /borrowed/id?id=1 

Gets you the borrowed book with id=1

#### GET /categories 
Gets you all the categories of books.

#### GET /categories/book
Parameters:
* title (str)
* author (str)

Example usage:
* /categories/book?title=Coś%20się%20kończy,%20coś%20się%20zaczyna&author=Andrzej%20Sapkowski

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
Gets you all the users.

#### GET /users/user
Parameters:
* login (str)

Example usage:
* /users/user?login=achudy 

Gets you only the user with login "achudy"


## POST

#### POST /books
Form data: 
* title (str)
* author (str)
* for_adults (int)
* library_branch (int)
* category_names (str) 

Posts a book.

#### POST /borrowed
Form data: 
* user_id (int)
* book_instance_id (int)
* start_time (date e.g. 2021-06-09)
* end_time (date)

Posts a borrowed record.

#### POST /categories
Form data: 
* category_name (str)

Posts a category.

#### POST /branches
Form data: 
* address (str)
* library_branch_name (str)

Posts a library branch.

#### POST /users
Form data: 
* name (str)
* surname (str)
* login (str)
* password (str)
* birth_date (date)
* user_type (str)

Posts a user.

## PUT

#### PUT /books
Form data: 
* id (int)
* author (str)
* for_adults (str)
* title (int)

Updates a book.

#### PUT /borrowed
Form data: 
* id (int)
* user_id (int)
* book_instance_id (int)
* start_time (date e.g. 2021-06-09)
* end_time (date)

Updates a borrowed record.

#### PUT /categories
Form data: 
* id (int)
* category_name (str)

Updates a category.

#### PUT /branches
Form data: 
* id (int)
* address (str)
* library_branch_name (str)

Updates a library branch.

#### PUT /users
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

#### DELETE /books
Parameters:
* id (int)

Example usage:
* /books?id=1

Deletes a book.

#### DELETE /borrowed
Parameters:
* id (int)

Deletes a borrowed record.

#### DELETE /categories
Parameters:
* id (int)

Deletes a category.

#### DELETE /branches
Parameters:
* id (int)

Deletes a library branch.

#### DELETE /users
Parameters:
* id (int)

Deletes a user.

