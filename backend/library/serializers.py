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
    score = serializers.FloatField(read_only=True)
    popularity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        exclude = ('id', 'creation_time')
        read_only_field = ('slug', 'score', 'popularity')


class AuthorSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(read_only=True)
    popularity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        exclude = ('id',)
        read_only_fields = ('slug', 'score', 'popularity')
