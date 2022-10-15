from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Author
from library.serializers import BookSerializer, AuthorSerializer

from .permissions import IsStaffOrReadOnly


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsStaffOrReadOnly,)


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsStaffOrReadOnly,)

    @action(methods=['GET'], detail=True)
    def books(self, request, pk=None):
        if pk is not None:
            serialized = BookSerializer(Book.objects.filter(author=pk), many=True)
            return Response(serialized.data)
        else:
            return Response(data='Primary key does not specified', status=status.HTTP_400_BAD_REQUEST)
