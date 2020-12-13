from components.ma import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'login', 'password', 'birth_date', 'user_type')
