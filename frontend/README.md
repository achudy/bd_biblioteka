# Library API for Databases Project AGH

## GET
#### /books
'id', 'fk_branch_id', 'fk_category_id', 'author', 'for_adults', 'title'
#### /books/\<id>
'id', 'fk_branch_id', 'fk_category_id', 'author', 'for_adults', 'title'
#### /borrowed
'id', 'fk_book_id', 'fk_user_id', 'start_time', 'end_time'
#### /borrowed/\<id>
'id', 'fk_book_id', 'fk_user_id', 'start_time', 'end_time'
#### /category
'id', 'category_name'
#### /category/\<id>
'id', 'category_name'
#### /library_branch
'id', 'name', 'address'
#### /library_branch/\<id>
'id', 'name', 'address'
#### /user
'id', 'name', 'surname', 'login', 'password', 'birth_date', 'user_type'
#### /user/\<id>
'id', 'name', 'surname', 'login', 'password', 'birth_date', 'user_type'

## PUT
#### /books/\<id>
'fk_branch_id', 'fk_category_id', 'author', 'for_adults', 'title'
#### /borrowed/\<id>
'fk_book_id', 'fk_user_id', 'start_time', 'end_time'
#### /category/\<id>
'category_name'
#### /library_branch/\<id>
'name', 'address'
#### /user/\<id>
'name', 'surname', 'login', 'password', 'birth_date', 'user_type'

## DELETE
#### /books/\<id>
#### /borrowed/\<id>
#### /category/\<id>
#### /library_branch/\<id>
#### /user/\<id>

## POST
#### /books
'fk_branch_id', 'fk_category_id', 'author', 'for_adults', 'title'
#### /borrowed
'fk_book_id', 'fk_user_id', 'start_time', 'end_time'
#### /category
'category_name'
#### /library_branch
''name', 'address'
#### /user
'name', 'surname', 'login', 'password', 'birth_date', 'user_type'
