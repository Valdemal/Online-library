from rest_framework import serializers

from library.models import Book
from user.models import User, Comment, Reading


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'photo', 'is_staff')
        read_only_fields = ('username', 'email', 'is_staff')


class CommentGetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=True, slug_field='slug')
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'book', 'user', 'score', 'text')
        read_only_fields = ('id', 'score', 'text')


class CommentSetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=False, slug_field='slug', queryset=Book.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('book', 'user', 'score', 'text')


class ReadingGetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=True, slug_field='slug')
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Reading
        fields = ('id', 'user', 'book')


class ReadingSetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=False, slug_field='slug', queryset=Book.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reading
        fields = ('id', 'book', 'user')
