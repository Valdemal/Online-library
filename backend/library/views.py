from rest_framework.viewsets import ModelViewSet

from library.filters import BookFilter, AuthorFilter
from library.models import Book, Author, Genre
from library.serializers import BookSerializer, AuthorSerializer, GenreSerializer
from main.permissions import IsStaffOrReadOnly


class BookViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
    filterset_class = BookFilter


class AuthorViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
    filterset_class = AuthorFilter


class GenreViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
