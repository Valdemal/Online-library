import pytest
from django.conf import settings

from user.models import User


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_library_db',
        'USER': 'test_admin',
        'PASSWORD': 'test_pass_12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }


@pytest.fixture
def staff_user(db) -> User:
    return User.objects.create_user(
        username='staff_user', email='test1@gmail.com',
        password='testpass1', is_staff=True
    )


@pytest.fixture
def simple_user(db) -> User:
    return User.objects.create_user(
        username='simple_user', email='test2@gmail.com', password='testpass1'
    )
