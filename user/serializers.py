from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'photo', 'first_name', 'last_name', 'is_staff')
