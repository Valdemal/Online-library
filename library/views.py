from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Author, Genre
from library.serializers import BookSerializer, AuthorSerializer, GenreSerializer
from main.permissions import IsStaffOrReadOnly
from user.models import Comment
from user.serializers import CommentSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
    lookup_field = 'slug'

    @action(methods=['GET'], detail=True)
    def comments(self, request, slug=None):
        if slug is not None:
            serialized = CommentSerializer(Comment.objects.filter(book__slug=slug), many=True)
            return Response(serialized.data)
        else:
            return Response(data='Book slug does not specified', status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
    lookup_field = 'slug'

    @action(methods=['GET'], detail=True)
    def books(self, request, slug=None):
        if slug is not None:
            serialized = BookSerializer(Book.objects.filter(author__slug=slug), many=True)
            return Response(serialized.data)
        else:
            return Response(data='Author slug does not specified', status=status.HTTP_400_BAD_REQUEST)


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsStaffOrReadOnly,)
    lookup_field = 'slug'

    @action(methods=['GET'], detail=True)
    def books(self, request, slug=None):
        if slug is not None:
            serialized = BookSerializer(Book.objects.filter(genres__slug__exact=slug), many=True)
            return Response(serialized.data)
        else:
            return Response(data='Genre slug does not specified', status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def authors(self, request, slug=None):
        if slug is not None:
            queryset = Author.objects.filter(book__genres__slug__exact=slug).distinct()
            serialized = AuthorSerializer(queryset, many=True)
            return Response(serialized.data)
        else:
            return Response(data='Genre slug does not specified', status=status.HTTP_400_BAD_REQUEST)
