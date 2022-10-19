from datetime import datetime

from django.core.validators import (
    MaxValueValidator, FileExtensionValidator,
    MinValueValidator, validate_image_file_extension
)
from django.db import models

from main import settings


class Book(models.Model):
    UPLOAD_ROOT = 'books/'

    title = models.CharField(
        max_length=255, verbose_name='Название'
    )

    creation_time = models.DateField(
        auto_now_add=True, verbose_name='Дата создания записи'
    )

    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, verbose_name='Автор'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    file = models.FileField(
        verbose_name='Файл', upload_to=UPLOAD_ROOT + 'files/',
        validators=[
            FileExtensionValidator(allowed_extensions=('pdf', 'docx'))
        ]
    )

    year_of_writing = models.IntegerField(
        null=True, verbose_name='Год написания',
        validators=[
            MaxValueValidator(datetime.now().year),
        ],
    )

    cover = models.ImageField(
        verbose_name='Обложка', blank=True, upload_to=UPLOAD_ROOT + 'covers/',
        validators=[
            validate_image_file_extension
        ]
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-creation_time']
        unique_together = [('title', 'author')]


class Author(models.Model):
    UPLOAD_ROOT = 'authors/'

    name = models.CharField(
        max_length=300, verbose_name='Имя',
    )

    surname = models.CharField(
        max_length=300, verbose_name='Фамилия',
    )

    image = models.ImageField(
        verbose_name='Портрет', blank=True, upload_to=UPLOAD_ROOT + 'images/',
        validators=[
            validate_image_file_extension
        ]
    )

    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.surname}'

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        unique_together = [('name', 'surname')]


class Comment(models.Model):
    score = models.FloatField(null=True, verbose_name='Оценка', validators=[
        MaxValueValidator(5), MinValueValidator(1),
    ])
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        unique_together = [('user', 'book')]
