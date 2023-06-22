from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from library.filters import BookFilter, AuthorFilter
from library.models import Book, Author, Genre
from library.serializers import BookSerializer, AuthorSerializer, GenreSerializer
from main.permissions import IsStaffOrReadOnly


class BookViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = IsStaffOrReadOnly,
    ordering_fields = 'title', 'year_of_writing', 'author'
    search_fields = 'title', 'author__name', 'author__surname'
    filter_backends = DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    filterset_class = BookFilter


class AuthorViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = IsStaffOrReadOnly,
    ordering_fields = 'name', 'surname'
    search_fields = 'name', 'surname'
    filter_backends = DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    filterset_class = AuthorFilter


class GenreViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = IsStaffOrReadOnly,
    ordering_fields = 'name',
    search_fields = 'name',
    filter_backends = filters.OrderingFilter, filters.SearchFilter

