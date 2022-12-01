from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='slug')

    class Meta:
        model = Book
        fields = ('slug', 'title', 'year_of_writing', 'author', 'description', 'file', 'cover')
        read_only_field = ('slug', 'author')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('slug', 'name', 'surname', 'image', 'description')
        read_only_fields = ('slug',)