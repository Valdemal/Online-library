from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from django.db import models


class User(AbstractUser):
    PHOTO_UPLOAD_ROOT = 'images/'

    photo = models.ImageField(
        verbose_name='Фото', blank=True, upload_to=PHOTO_UPLOAD_ROOT,
        validators=[
            validate_image_file_extension
        ]
    )

    def delete(self, using=None, keep_parents=False):
        self.photo.delete()
        super(User, self).delete(using, keep_parents)
