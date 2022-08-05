from django.test import TestCase

from library.models import Author
from library.serializers import AuthorSerializer


class TestAuthorSerializers(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.valid_data_cases = [
            {'name': "Владимир",
             'surname': 'Сорокин',
             'description': 'Русский альтернативный писатель',
             },
            #     Добавить поле с картинкой
        ]

        cls.invalid_data_cases = [
            {},
            {'name': 'Владимир', 'surname': 'Сорокин'},
            {'name': "Владимир", 'description': 'Русский альтернативный писатель', },
            {'surname': 'Сорокин', 'description': 'Русский альтернативный писатель', },
            {'name': "", 'surname': '', 'description': '', },
            {'name': "Владимир", 'surname': "", 'description': 'Русский альтернативный писатель'},
            {'name': 'Владимир', 'surname': 'Сорокин', 'description': ""},
            {'name': "", 'surname': 'Сорокин', 'description': 'Русский альтернативный писатель'},
        ]

    def test_valid_creation(self):
        for case in self.valid_data_cases:
            with self.subTest(case=case):
                serializer = AuthorSerializer(data=case)
                self.assertTrue(serializer.is_valid())

    def test_invalid_creation(self):
        for case in self.invalid_data_cases:
            with self.subTest(case=case):
                serializer = AuthorSerializer(data=case)
                self.assertFalse(serializer.is_valid())

    def test_unique_validation(self):
        data = {'name': 'Виктор', 'surname': 'Пелевин', 'description': "Писатель"}
        Author.objects.create(**data)
        serializer = AuthorSerializer(data=data)
        self.assertFalse(serializer.is_valid())
