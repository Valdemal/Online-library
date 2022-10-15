from user.models import User

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from library.models import Author, Book
from library.serializers import BookSerializer, AuthorSerializer
from library.test.test_serializers import create_file


class BooksAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name='Виктор', surname='Пелевин',
                                           description="Писатель")

        cls.books_data_set = [
            {
                'title': 'Generation П', 'author': cls.author,
                'description': "Роман", 'file': create_file('pdf'),
                'year_of_writing': 1999
            },
            {
                'title': 'Чапаев и пустота', 'author': cls.author,
                'description': "Роман", 'file': create_file('pdf')
            },
        ]

        cls.staff_user = User.objects.create(
            username='staff_user', email='test1@gmail.com',
            password='testpass1', is_staff=True
        )

        cls.simple_user = User.objects.create(
            username='simple_user', email='test2@gmail.com', password='testpass1'
        )

    def test_GET_list(self):
        """Тестирование GET-запроса получающего список всех книг"""

        for book_data in self.books_data_set:
            Book.objects.create(**book_data)

        # Получение данных путем создания запроса
        url = reverse('api:books-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Получение данных из сериализатора напрямую (обязательно передавать
        # request в context для формирования корректного url адреса файла)
        request = response.wsgi_request
        serializer = BookSerializer(
            Book.objects.all(), many=True,
            context={'request': request}
        )

        self.assertEqual(serializer.data, response.data)

    def test_GET_detail(self):
        """Тестирование GET-запроса получающего конкретную книгу по id"""

        book = Book.objects.create(**self.books_data_set[0])

        url = reverse('api:books-detail', kwargs={'pk': book.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        request = response.wsgi_request
        serializer = BookSerializer(
            instance=book, context={'request': request}
        )

        self.assertEqual(serializer.data, response.data)

    def test_POST_incorrect_permission(self):
        """
        Тестирование запроса с корректными данными от клиента
        не обладающего необходимыми правами
        """

        # Клиент не зарегистрирован
        data = self._get_valid_request_book_data()
        response = self.client.post(reverse('api:books-list'), data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Клиент зарегистрирован, но не является персоналом
        self.client.force_login(self.simple_user)
        response = self.client.post(reverse('api:books-list'), data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_POST_correct_data_and_permissions(self):
        """
        Тестирование запроса с корректными данными от клиента
        обладающего необходимыми правами
        """
        self.client.force_login(user=self.staff_user)
        data = self._get_valid_request_book_data()
        response = self.client.post(reverse('api:books-list'), data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка данных ответа
        request = response.wsgi_request
        serializer = BookSerializer(
            instance=Book.objects.get(author_id=data['author']),
            context={'request': request}
        )

        self.assertEqual(serializer.data, response.data)

    def test_POST_incorrect_data_and_correct_permissions(self):
        """
        Тестирование запроса с некорректными данными от клиента
        обладающего необходимимы правами
        """
        self.client.force_login(user=self.staff_user)
        data = self._get_invalid_request_book_data()
        response = self.client.post(reverse('api:books-list'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def tearDown() -> None:
        for book in Book.objects.all():
            book.delete()

    def _get_valid_request_book_data(self) -> dict:
        data = {
            'title': 'Generation П',
            'author': self.author.id,
            'description': "Роман",
            'file': create_file('pdf'),
            'year_of_writing': 1999
        }

        BookSerializer(data=data).is_valid(raise_exception=True)

        return data

    def _get_invalid_request_book_data(self):
        data = {
            'author': self.author.id,
            'description': "Роман",
            'file': create_file('pdf'),
            'year_of_writing': 1999
        }

        assert not BookSerializer(data=data).is_valid(), \
            'Data is valid, but function must return invalid data'

        return data


class AuthorApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.authors_data_set = [
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

        cls.staff_user = User.objects.create(
            username='staff_user', email='test1@gmail.com',
            password='testpass1', is_staff=True
        )

        cls.simple_user = User.objects.create(
            username='simple_user', email='test2@gmail.com', password='testpass1'
        )

    @staticmethod
    def tearDown() -> None:
        for author in Author.objects.all():
            author.delete()

    def test_GET_list(self):
        for data_set in self.authors_data_set:
            Author.objects.create(**data_set)

        url = reverse('api:authors-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = AuthorSerializer(
            instance=Author.objects.all(), many=True,
            context={'request': response.wsgi_request}
        ).data

        self.assertEqual(response.data, serialized_data)

    def test_GET_detail(self):
        author = Author.objects.create(**self.authors_data_set[1])

        url = reverse('api:authors-detail', kwargs={'pk': author.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = AuthorSerializer(
            instance=author, context={'request': response.wsgi_request}
        )

        self.assertEqual(response.data, serializer.data)

    def test_POST_correct_data_and_permissions(self):
        self.client.force_login(self.staff_user)
        url = reverse('api:authors-list')

        for author in self.authors_data_set:
            with self.subTest(case=author):
                response = self.client.post(url, data=author)

                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

                # Проверка данных ответа
                serializer = AuthorSerializer(
                    instance=Author.objects.get(pk=response.data['id']),
                    context={'request': response.wsgi_request}
                )

                self.assertEqual(response.data, serializer.data)
