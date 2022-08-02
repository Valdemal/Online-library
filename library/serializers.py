from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'year_of_writing', 'author', 'description')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'surname', 'image', 'description')

    def create(self, validated_data: dict) -> Author:
        return Author.objects.create(**validated_data)

    def update(self, instance: Author, validated_data: dict) -> Author:
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        return instance
