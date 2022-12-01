# Generated by Django 4.1.2 on 2022-11-30 23:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creation_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]