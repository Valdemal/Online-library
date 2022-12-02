from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension, MinValueValidator, MaxValueValidator
from django.db import models

from library.models import Book
from main import settings


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


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)
    score = models.FloatField(null=True, verbose_name='Оценка', validators=[
        MaxValueValidator(5), MinValueValidator(1),
    ])
    text = models.TextField(verbose_name='Текст')
    creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        unique_together = [('user', 'book')]
        ordering = ['-creation_time']


class Reading(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Чтение'
        verbose_name_plural = 'Чтения'
        unique_together = [('user', 'book')]
        ordering = ['-creation_time']
