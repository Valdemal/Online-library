from django_filters import rest_framework as drf_filters
from django_filters.constants import EMPTY_VALUES

from library.models import Book, Author


class FullEntryFilter(drf_filters.CharFilter, drf_filters.BaseInFilter):
    """
    Фильтр для отношения многие-ко-многим, который проверяет вхождение всех
    значений фильтра в ManyToManyField значение.
    """

    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        if self.distinct:
            qs = qs.distinct()

        method = self.get_method(qs)
        res = method(**{self.field_name: value[0]})

        for i in range(1, len(value)):
            res &= method(**{self.field_name: value[i]})

        return res


class BookFilter(drf_filters.FilterSet):
    genres = FullEntryFilter(field_name='genres__slug', distinct=True, label='Жанр')
    year_of_writing = drf_filters.RangeFilter()
    author = drf_filters.CharFilter(field_name='author__slug')

    class Meta:
        model = Book
        fields = ['genres', 'author', 'year_of_writing']


class AuthorFilter(drf_filters.FilterSet):
    genres = FullEntryFilter(field_name='book__genres__slug', distinct=True, label='Жанр')

    class Meta:
        model = Author
        fields = ['genres']
