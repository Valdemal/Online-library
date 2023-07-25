import pytest

from library.serializers import AuthorSerializer

@pytest.mark.django_db
def test_valid_data_cases(author_valid_data):
    serializer = AuthorSerializer(data=author_valid_data)

    assert serializer.is_valid()


@pytest.mark.parametrize('data', 'author_invalid_data')
def test_invalid_data_cases(data):
    serializer = AuthorSerializer(data=data)

    assert not serializer.is_valid()


def test_unique_validation(author):
    data = {
        'name': author.name, 'surname': author.surname, 'description': author.description
    }
    serializer = AuthorSerializer(data=data)

    assert not serializer.is_valid()
