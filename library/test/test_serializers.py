import os
import sys
import tempfile

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase

from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


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


class TestAuthorSerializers(TestCase):

    def test_valid_data_cases(self):
        valid_data_cases = [
            {
                'name': "Владимир", 'surname': 'Сорокин',
                'description': 'Русский альтернативный писатель',
            },
            {
                'name': 'Оскар', 'surname': 'Уальд',
                'description': 'Ирландский писатель',
                'image': create_file('jpg')
            }
        ]

        for case in valid_data_cases:
            with self.subTest(case=case):
                serializer = AuthorSerializer(data=case)
                self.assertTrue(serializer.is_valid())

    def test_invalid_data_cases(self):
        invalid_data_cases = [
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

        for case in invalid_data_cases:
            with self.subTest(case=case):
                serializer = AuthorSerializer(data=case)
                self.assertFalse(serializer.is_valid())

    def test_unique_validation(self):
        data = {'name': 'Виктор', 'surname': 'Пелевин', 'description': "Писатель"}
        Author.objects.create(**data)
        serializer = AuthorSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class TestBookSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name='Виктор', surname='Пелевин', description="Писатель")

    def test_valid_data_cases(self):
        valid_data_cases = [
            {
                'title': 'Generation П',
                'author': self.author.id,
                'description': "Роман",
                'file': create_file('pdf'),
                'year_of_writing': 1999
            },
            {
                'title': 'Generation П',
                'author': self.author.id,
                'description': "Роман",
                'file': create_file('pdf')
            },
            {
                'title': 'Generation П',
                'author': self.author.id,
                'description': "Роман",
                'file': create_file('docx')
            }
        ]

        for case in valid_data_cases:
            with self.subTest(case=case):
                serializer = BookSerializer(data=case)
                self.assertTrue(serializer.is_valid())

    def test_invalid_data_cases(self):
        invalid_data_cases = [
            {},
            {
                'title': 'Над пропастью во ржи',
                'author': self.author.id,
                'description': 'Повесть про подростка',
                'file': None
            },
            {
                'title': '',
                'author': self.author.id,
                'description': 'Повесть про подростка',
                'file': create_file('pdf')
            },
            {
                'title': 'Над пропастью во ржи',
                'author': None,
                'description': 'Повесть про подростка',
                'file': create_file('pdf')
            },
            {
                'title': 'Generation П',
                'author': self.author.id,
                'description': "",
                'file': create_file('pdf')
            },
        ]

        for case in invalid_data_cases:
            with self.subTest(case=case):
                serializer = BookSerializer(data=case)
                self.assertFalse(serializer.is_valid())

    def test_unique_validation(self):
        data = {
            'title': 'Generation П',
            'author': self.author,
            'description': 'Роман',
            'file': create_file('pdf')
        }

        book = Book.objects.create(**data)
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        book.delete()
