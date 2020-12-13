from components.ma import ma


class LibraryBranchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address')
