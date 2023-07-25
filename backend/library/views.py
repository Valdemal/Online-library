from django.db.models import Avg, Count, Q, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from library.filters import BookFilter, AuthorFilter
from library.models import Book, Author, Genre
from library.serializers import BookSerializer, AuthorSerializer, GenreSerializer
from main.permissions import IsStaffOrReadOnly


class BookViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = BookSerializer
    queryset = Book.objects.annotate(
        score=Avg('comment__score', filter=Q(comment__book=F('id'))),
        popularity=Count('reading__id', filter=Q(reading__book=F('id')), distinct=True),
    )
    permission_classes = IsStaffOrReadOnly,
    ordering_fields = 'title', 'year_of_writing', 'author', 'popularity', 'score'
    ordering = '-popularity', '-score'
    search_fields = 'title', 'author__name', 'author__surname'
    filter_backends = DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    filterset_class = BookFilter
    parser_classes = MultiPartParser,


class AuthorViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = AuthorSerializer
    queryset = Author.objects.annotate(
        score=Avg('book__comment__score', filter=Q(book__comment__book=F('book'))),
        popularity=Count('book__reading', filter=Q(book__reading__book=F('book')), distinct=True)
    )
    permission_classes = IsStaffOrReadOnly,
    ordering_fields = 'name', 'surname', 'popularity', 'score'
    ordering = '-popularity', '-score'
    search_fields = 'name', 'surname'
    filter_backends = DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    filterset_class = AuthorFilter
    parser_classes = MultiPartParser,


class GenreViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = IsStaffOrReadOnly,
    ordering_fields = 'name',
    search_fields = 'name',
    filter_backends = filters.OrderingFilter, filters.SearchFilter
