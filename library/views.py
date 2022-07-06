from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book, Author
from library.serializers import BookSerializer, AuthorSerializer


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class AuthorAPIView(APIView):

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'author': serializer.data})

    def put(self, request, *args, **kwargs):
        primary_key = kwargs.get('pk')

        if primary_key is None:
            return Response({'errors': "Method PUT is not allowed."})

        try:
            author = Author.objects.get(pk=primary_key)
        except:
            return Response({'errors': "Object does not exists."})

        serializer = AuthorSerializer(data=request.data, instance=author)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)