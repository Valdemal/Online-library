from datetime import datetime

from django.core.validators import (
    MaxValueValidator, FileExtensionValidator,
    MinValueValidator, validate_image_file_extension
)
from django.db import models

from main import settings
from main.utils import slugify


class Author(models.Model):
    UPLOAD_ROOT = 'authors/'

    name = models.CharField(max_length=100, verbose_name='Имя', )

    surname = models.CharField(max_length=100, verbose_name='Фамилия', )

    slug = models.SlugField(max_length=220, unique=True, auto_created=True, verbose_name='URL')

    image = models.ImageField(
        verbose_name='Портрет', blank=True, upload_to=UPLOAD_ROOT + 'images/',
        validators=[validate_image_file_extension]
    )

    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.surname}'

    def save(self, *args, **kwargs):
        """Переделать, чтобы slug переделывался при изменении имени или фамилии"""

        self.slug = slugify(str(self))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        unique_together = [('name', 'surname')]


class Book(models.Model):
    UPLOAD_ROOT = 'books/'

    title = models.CharField(max_length=100, verbose_name='Название')

    creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания записи')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

    slug = models.SlugField(max_length=320, unique=True, auto_created=True, verbose_name='URL')

    description = models.TextField(verbose_name='Описание')

    file = models.FileField(
        verbose_name='Файл', upload_to=UPLOAD_ROOT + 'files/',
        validators=[FileExtensionValidator(allowed_extensions=('pdf', 'docx'))]
    )

    year_of_writing = models.IntegerField(
        null=True, verbose_name='Год написания',
        validators=[MaxValueValidator(datetime.now().year), ],
    )

    cover = models.ImageField(
        verbose_name='Обложка', blank=True, upload_to=UPLOAD_ROOT + 'covers/',
        validators=[validate_image_file_extension]
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Переделать, чтобы slug переделывался при изменении имени или фамилии"""

        self.slug = slugify(str(self) + " " + str(self.author))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-creation_time']
        unique_together = [('title', 'author')]


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
