from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, FileExtensionValidator

class Book(models.Model):
    FILE_UPLOAD_ROOT = 'books/'

    title = models.CharField(max_length=255, verbose_name='Название')

    creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания записи')

    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')

    description = models.TextField(verbose_name='Описание')

    file = models.FileField(verbose_name='Файл', upload_to=FILE_UPLOAD_ROOT, validators=[
        FileExtensionValidator(allowed_extensions=('pdf', 'docx'))
    ])

    year_of_writing = models.IntegerField(null=True, verbose_name='Год написания', validators=[
        MaxValueValidator(datetime.now().year),
    ], )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-creation_time']
        unique_together = [('title', 'author')]


class Author(models.Model):
    PHOTO_UPLOAD_ROOT = 'images/'

    name = models.CharField(max_length=300, verbose_name='Имя')
    surname = models.CharField(max_length=300, verbose_name='Фамилия')
    image = models.ImageField(verbose_name='Портрет', null=True, upload_to=PHOTO_UPLOAD_ROOT)
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
    score = models.FloatField(null=True)
    text = models.TextField()
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
