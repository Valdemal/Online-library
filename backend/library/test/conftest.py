import pytest
import os
import sys
import tempfile

from django.core.files.uploadedfile import InMemoryUploadedFile

from library.models import Author
from library.serializers import BookSerializer


class Helpers:
    @staticmethod
    def create_file(extension: str) -> InMemoryUploadedFile:
        filename = 'test.' + extension

        # Работает хреново, но идея правильная
        file = tempfile.NamedTemporaryFile(mode='rb+', suffix='.' + extension)
        file.write(os.urandom(1000))

        return InMemoryUploadedFile(
            file, None,
            filename, extension,
            sys.getsizeof(file), None
        )


AUTHOR_VALID_DATA = [
    {
        'name': "Владимир", 'surname': 'Сорокин',
        'description': 'Русский альтернативный писатель',
    },
    {
        'name': 'Оскар', 'surname': 'Уальд',
        'description': 'Ирландский писатель',
        'image': Helpers.create_file('jpg')
    }
]

AUTHOR_INVALID_DATA = [
    {},
    {'name': 'Владимир', 'surname': 'Сорокин'},
    {'name': "Владимир", 'description': 'Русский альтернативный писатель', },
    {'surname': 'Сорокин', 'description': 'Русский альтернативный писатель', },
    {'name': "", 'surname': '', 'description': '', },
    {'name': "Владимир", 'surname': "", 'description': 'Русский альтернативный писатель'},
    {'name': 'Владимир', 'surname': 'Сорокин', 'description': ""},
    {'name': "", 'surname': 'Сорокин', 'description': 'Русский альтернативный писатель'},
    {'name': "@dfafRd>", 'surname': 'Сорокин', 'description': 'Русский альтернативный писатель'},
    {'name': "Владимир", 'surname': 'Сорокин ', 'description': 'Русский альтернативный писатель'},
    {'name': "Вл. фыв", 'surname': 'Сорокин,dasfaa', 'description': 'Русский альтернативный писатель'},
]


@pytest.fixture
def helpers():
    return Helpers


@pytest.fixture
def author(db) -> Author:
    return Author.objects.create(name='Виктор', surname='Пелевин', description="Писатель")


@pytest.fixture
def books_data(author, helpers):
    return [
        {
            'title': 'Generation П', 'author': author,
            'description': "Роман", 'file': helpers.create_file('pdf'),
            'year_of_writing': 1999
        },
        {
            'title': 'Чапаев и пустота', 'author': author,
            'description': "Роман", 'file': helpers.create_file('pdf')
        },
    ]


@pytest.fixture(scope='session', params=AUTHOR_VALID_DATA)
def author_valid_data(request):
    return request.param


@pytest.fixture(scope='session')
def author_invalid_data():
    return AUTHOR_INVALID_DATA


@pytest.fixture
def valid_request_book_data(books_data):
    data = books_data[0]
    BookSerializer(data=data).is_valid(raise_exception=True)

    return data


@pytest.fixture
def invalid_request_book_data(author, helpers):
    data = {
        'author': author.id,
        'description': "Роман",
        'file': helpers.create_file('pdf'),
        'year_of_writing': 1999
    }

    assert not BookSerializer(data=data).is_valid(), \
        'Data is valid, but function must return invalid data'

    return data
