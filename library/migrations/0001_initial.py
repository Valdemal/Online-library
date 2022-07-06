# Generated by Django 4.0.5 on 2022-06-09 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('surname', models.CharField(max_length=300, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('creation_time', models.DateField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-creation_time'],
            },
        ),
    ]
