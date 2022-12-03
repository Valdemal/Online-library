from rest_framework import serializers

from .models import Book, Author, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')
        read_only_fields = ('slug',)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, queryset=Author.objects.all(), slug_field='slug')
    genres = GenreSerializer(many=True, required=False)  # Оно как-то само фильтрует, я в шоке!

    class Meta:
        model = Book
        fields = ('slug', 'title', 'year_of_writing', 'author', 'description', 'file', 'cover', 'genres')
        read_only_field = ('slug',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('slug', 'name', 'surname', 'image', 'description')
        read_only_fields = ('slug',)