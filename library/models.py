from datetime import datetime

from django.core.validators import (
    MaxValueValidator, FileExtensionValidator,
    validate_image_file_extension
)
from django.db import models

from main.utils import slugify_unicode

def get_model_with_slug(slug_max_len: int):
    """
    Возвращает абстрактную модель с уже "вшитым" полем slug
    @param slug_max_len: максимальная длина поля slug
    """

    class SlugModel(models.Model):
        slug = models.SlugField(max_length=slug_max_len, unique=True, auto_created=True, verbose_name='URL')

        def slugify(self) -> str:
            return slugify_unicode(str(self))

        def save(self, *args, **kwargs):
            self.slug = self.slugify()
            super().save(*args, **kwargs)

        class Meta:
            abstract = True

    return SlugModel


class Author(get_model_with_slug(220)):
    UPLOAD_ROOT = 'authors/'

    name = models.CharField(max_length=100, verbose_name='Имя', )

    surname = models.CharField(max_length=100, verbose_name='Фамилия', )

    image = models.ImageField(
        verbose_name='Портрет', blank=True, upload_to=UPLOAD_ROOT + 'images/',
        validators=[validate_image_file_extension]
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


class Genre(get_model_with_slug(100)):
    name = models.CharField(max_length=70, unique=True, verbose_name='Название')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(get_model_with_slug(302)):
    UPLOAD_ROOT = 'books/'

    title = models.CharField(max_length=100, verbose_name='Название')

    creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания записи')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

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

    def slugify(self) -> str:
        return slugify_unicode(str(self) + " " + str(self.author))

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-creation_time']
        unique_together = [('title', 'author')]
