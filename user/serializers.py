from rest_framework import serializers

from user.models import User, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'photo', 'first_name', 'last_name', 'is_staff')


class CommentSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=True, slug_field='slug')
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'book', 'score', 'text')
