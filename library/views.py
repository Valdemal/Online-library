from typing import Callable

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Author, Genre
from library.serializers import BookSerializer, AuthorSerializer, GenreSerializer

from main.permissions import IsStaffOrReadOnly

from user.models import Comment
from user.serializers import CommentSerializer


class SlugRoutedModelViewSet(ModelViewSet):
    """
    ModelViewSet в котором поиск объектов модели осуществляется по slug.
    Модель вьюсета должна иметь поле slug!!!
    """
    lookup_field = 'slug'

    @staticmethod
    def get_response_by_slug(get_queryset_by_slug: Callable, serializer_class, slug=None) -> Response:
        """
        Возвращает ответ в виде сериализованных данных полученных по слагу.
        @param get_queryset_by_slug: функция, возвращающая выборку на основе слага
        @param serializer_class: класс сериализующий выборку
        @param slug: слаг
        """

        if slug is not None:
            serialized = serializer_class(get_queryset_by_slug(slug), many=True)
            return Response(serialized.data)
        else:
            return Response(
                data='Slug does not specified',
                status=status.HTTP_400_BAD_REQUEST
            )


class BookViewSet(SlugRoutedModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsStaffOrReadOnly,)

    @action(methods=['GET'], detail=True)
    def comments(self, request, slug=None):
        return self.get_response_by_slug(
            lambda slug: Comment.objects.filter(book__slug=slug),
            CommentSerializer, slug
        )


class AuthorViewSet(SlugRoutedModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsStaffOrReadOnly,)

    @action(methods=['GET'], detail=True)
    def books(self, request, slug=None):
        return self.get_response_by_slug(
            lambda slug: Book.objects.filter(author__slug=slug),
            BookSerializer, slug
        )


class GenreViewSet(SlugRoutedModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsStaffOrReadOnly,)

    @action(methods=['GET'], detail=True)
    def books(self, request, slug=None):
        return self.get_response_by_slug(
            lambda slug: Book.objects.filter(genres__slug__exact=slug),
            BookSerializer, slug
        )

    @action(methods=['GET'], detail=True)
    def authors(self, request, slug=None):
        return self.get_response_by_slug(
            lambda slug: Author.objects.filter(book__genres__slug__exact=slug).distinct(),
            AuthorSerializer, slug
        )
