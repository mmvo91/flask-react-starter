from api import models
from ..extensions import ma


class User(ma.ModelSchema):
    class Meta:
        model = models.User
        fields = [
            'id',
            'username',
            'last_login'
        ]
