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
        fields = '__all__'
        read_only_fields = ('id', 'score', 'text')


class CommentSetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=False, slug_field='slug', queryset=Book.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class ReadingGetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=True, slug_field='slug')
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Reading
        exclude = ('creation_time',)


class ReadingSetSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=False, read_only=False, slug_field='slug', queryset=Book.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reading
        exclude = ('creation_time', )
