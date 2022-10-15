# Generated by Django 4.0.5 on 2022-08-05 13:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_remove_book_release_date_book_year_of_writing'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(default='Русский писатель', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Портрет'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Русский писатель', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default='Русский писатель', upload_to='books/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('pdf', 'docx'))], verbose_name='Файл'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('name', 'surname')},
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author')},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Оценка')),
                ('text', models.TextField(verbose_name='Текст')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Книга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'unique_together': {('user', 'book')},
            },
        ),
    ]