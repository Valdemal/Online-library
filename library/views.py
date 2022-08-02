from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .services import AuthorService


def index(request):
    return render(request, 'index.html')


def authors(request):
    return render(request, 'authors.html')


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()


class AuthorAPIView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        return Response(data="Get запрос пока не определен")

    @staticmethod
    def post(request) -> Response:
        try:
            return Response(AuthorService.create(request.data))
        except ValidationError:
            return Response(data="Invalid data")

    @staticmethod
    def put(request, *args, **kwargs) -> Response:
        primary_key = kwargs.get('pk')

        if primary_key is None:
            return Response(data="Primary key does not specified")

        try:
            return Response(data=AuthorService.update(request.data, primary_key))
        except ValidationError:
            return Response(data="Invalid data")
        except ObjectDoesNotExist:
            return Response(data="Author does not exists")
