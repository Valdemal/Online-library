import os
import dotenv
from pathlib import Path

from main.utils import JsonFormatter

# Подгружаем переменные окружения
dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = eval(os.getenv('ALLOWED_HOSTS'))

# Application definition


INSTALLED_APPS = [
    # Стандартные приложения django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние пакеты
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_csv',
    'djoser',
    'corsheaders',
    'drf_yasg',
    'django_filters',

    # Внутренние приложения
    'library.apps.LibraryConfig',
    'user.apps.UserConfig',
    'services',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if os.getenv('DATABASE') == 'postgres':
    default_db_settings = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
else:
    default_db_settings = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

DATABASES = {
    'default': default_db_settings
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = os.getenv('TZ')

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR.parent / 'static/'
STATIC_URL = 'static/'

# Media files

MEDIA_ROOT = BASE_DIR.parent / 'media/'
MEDIA_URL = '/media/'

# logging

LOG_FILES_DIR = BASE_DIR.parent / 'logs/'
DEFAULT_LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'main': {
            'format': '[{levelname}]({asctime}) - {message}',
            'style': '{',
        },
        'json_formatter': {
            '()': JsonFormatter,
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'main',
        },
        'django_file': {
            'class': 'logging.FileHandler',
            'filename': str(LOG_FILES_DIR / 'django.json'),
            'formatter': 'json_formatter',
        },
        'celery_file':  {
            'class': 'logging.FileHandler',
            'filename': str(LOG_FILES_DIR / 'celery.json'),
            'formatter': 'json_formatter',
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console', 'django_file'],
            'level': DEFAULT_LOG_LEVEL,
            'propagate': True
        },
        'celery': {
            'handlers': ['console', 'celery_file'],
            'level': DEFAULT_LOG_LEVEL,
            'propagate': True
        }
    }
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework_csv.parsers.CSVParser'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

DJOSER = {
    'SERIALIZERS': {
        'user': 'user.serializers.UserSerializer',
        'current_user': 'user.serializers.UserSerializer',
    }
}

# corsheaders

CORS_ORIGIN_ALLOW_ALL = True

# celery
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_BROKER_URL')
# в crontab всегда используется utc даже если изменить timezone
CELERY_TIMEZONE = 'UTC'
