from components.ma import ma


class BorrowedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fk_book_id', 'fk_user_id', 'start_time', 'end_time')
