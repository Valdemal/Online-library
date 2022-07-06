from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания записи')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    year_of_writing = models.IntegerField(validators=[
        MaxValueValidator(datetime.now().year),
    ], null=True, verbose_name='Год написания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-creation_time']


class Author(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя')
    surname = models.CharField(max_length=300, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
