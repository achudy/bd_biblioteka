from components.ma import ma


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'category_name')
