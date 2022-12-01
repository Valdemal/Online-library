from datetime import datetime

from django.core.validators import (
    MaxValueValidator, FileExtensionValidator,
    validate_image_file_extension
)
from django.db import models

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


class Genre(models.Model):
    name = models.CharField(max_length=70, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, auto_created=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


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

    genres = models.ManyToManyField(Genre)

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

