from django_filters import rest_framework as drf_filters

from user.models import Reading, Comment


class ReadingFilter(drf_filters.FilterSet):
    book = drf_filters.CharFilter(field_name='book__slug')
    user = drf_filters.CharFilter(field_name='user__username')

    class Meta:
        model = Reading
        fields = ['user', 'book']


class CommentFilter(drf_filters.FilterSet):
    book = drf_filters.CharFilter(field_name='book__slug')
    user = drf_filters.CharFilter(field_name='user__username')
    score = drf_filters.RangeFilter()

    class Meta:
        model = Comment
        fields = ['user', 'book', 'score']
