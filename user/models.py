from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from django.db import models


class User(AbstractUser):
    UPLOAD_ROOT = 'users/'

    photo = models.ImageField(
        verbose_name='Фото', blank=True, upload_to=UPLOAD_ROOT + 'photos/',
        validators=[
            validate_image_file_extension
        ]
    )

    is_active = models.BooleanField(verbose_name='Статус активности', default=False)

    email = models.EmailField(verbose_name="Адрес электронной почты")

    def delete(self, using=None, keep_parents=False):
        self.photo.delete()
        super(User, self).delete(using, keep_parents)
