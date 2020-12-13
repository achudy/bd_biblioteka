from components.ma import ma


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fk_branch_id', 'fk_category_id', 'author', 'for_adults', 'title')
