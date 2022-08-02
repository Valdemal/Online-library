from .models import Author
from .serializers import AuthorSerializer


class AuthorService:
    @staticmethod
    def create(data: dict) -> dict:
        serializer = AuthorSerializer(data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def update(data: dict, primary_key: int) -> dict:
        author = Author.objects.get(pk=primary_key)
        serializer = AuthorSerializer(data=data, instance=author)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data
