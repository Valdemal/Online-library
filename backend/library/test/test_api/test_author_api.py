from rest_framework import status
from rest_framework.reverse import reverse

from library.models import Author
from library.serializers import AuthorSerializer


def test_list_request(client, authors_data):
    for data_set in authors_data:
        Author.objects.create(**data_set)

    url = reverse('api:authors-list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

    serialized_data = AuthorSerializer(
        instance=Author.objects.all(), many=True,
        context={'request': response.wsgi_request}
    ).data

    assert response.data == serialized_data


def test_retrieve_request(client, authors_data):
    author = Author.objects.create(**authors_data[1])

    url = reverse('api:authors-detail', kwargs={'pk': author.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

    serializer = AuthorSerializer(
        instance=author, context={'request': response.wsgi_request}
    )

    assert response.data == serializer.data


# def test_create_with_correct_data_and_permissions(client, staff_user):
    # client.force_login(staff_user)
    # url = reverse('api:authors-list')

    # параметризовать
    # for author in self.authors_data_set:
    #     with self.subTest(case=author):
    #         response = self.client.post(url, data=author)
    #
    #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #         # Проверка данных ответа
    #         serializer = AuthorSerializer(
    #             instance=Author.objects.get(pk=response.data['id']),
    #             context={'request': response.wsgi_request}
    #         )
    #
    #         self.assertEqual(response.data, serializer.data)