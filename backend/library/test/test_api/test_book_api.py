from rest_framework import status
from rest_framework.reverse import reverse

from library.models import Book
from library.serializers import BookSerializer


def test_list_request(client, books_data):
    """Тестирование GET-запроса получающего список всех книг"""

    for book_data in books_data:
        Book.objects.create(**book_data)

    # Получение данных путем создания запроса
    url = reverse('api:books-list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

    # Получение данных из сериализатора напрямую (обязательно передавать
    # request в context для формирования корректного url адреса файла)
    request = response.wsgi_request
    serializer = BookSerializer(
        Book.objects.all(), many=True,
        context={'request': request}
    )

    assert serializer.data == response.data


def test_retrieve_request(client, books_data):
    """Тестирование GET-запроса получающего конкретную книгу по id"""

    book = Book.objects.create(**books_data[0])

    url = reverse('api:books-detail', kwargs={'pk': book.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

    request = response.wsgi_request
    serializer = BookSerializer(
        instance=book, context={'request': request}
    )

    assert serializer.data == response.data


def test_create_with_correct_data_and_permission(client, staff_user, valid_request_book_data):
    """
         Тестирование запроса с корректными данными от клиента
         обладающего необходимыми правами
         """
    client.force_login(user=staff_user)
    response = client.post(reverse('api:books-list'), valid_request_book_data)

    # Проверка статуса ответа
    assert response.status_code == status.HTTP_201_CREATED

    # Проверка данных ответа
    request = response.wsgi_request
    serializer = BookSerializer(
        instance=Book.objects.get(author_id=valid_request_book_data['author']),
        context={'request': request}
    )

    assert serializer.data == response.data


def test_create_with_incorrect_permission(client, simple_user, valid_request_book_data):
    """
    Тестирование запроса с корректными данными от клиента
    не обладающего необходимыми правами
    """

    response = client.post(reverse('api:books-list'), data=valid_request_book_data)

    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Клиент зарегистрирован, но не является персоналом
    client.force_login(simple_user)
    response = client.post(reverse('api:books-list'), data=valid_request_book_data)

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_create_with_incorrect_data_and_correct_permissions(client, staff_user, invalid_request_book_data):
    """
    Тестирование запроса с некорректными данными от клиента
    обладающего необходимыми правами
    """
    client.force_login(user=staff_user)
    response = client.post(reverse('api:books-list'), invalid_request_book_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
