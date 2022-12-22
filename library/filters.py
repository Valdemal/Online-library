from django_filters import rest_framework as drf_filters

from library.models import Book, Author


class CharBaseInFilter(drf_filters.CharFilter, drf_filters.BaseInFilter):
    pass


class BookFilter(drf_filters.FilterSet):
    genres = CharBaseInFilter(field_name='genres__slug', lookup_expr='in', distinct=True)
    year_of_writing = drf_filters.RangeFilter()
    author = drf_filters.CharFilter(field_name='author__slug')

    class Meta:
        model = Book
        fields = ['genres', 'author', 'year_of_writing']


class AuthorFilter(drf_filters.FilterSet):
    genres = CharBaseInFilter(field_name='book__genres__slug', lookup_expr='in', distinct=True, label='Жанр')

    class Meta:
        model = Author
        fields = ['genres']
