# Generated by Django 4.1.2 on 2023-01-14 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_alter_book_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_writing',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2023)], verbose_name='Год написания'),
        ),
    ]
