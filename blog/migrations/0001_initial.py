# Generated by Django 4.2.6 on 2023-10-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью (изображение)')),
                ('creation_data', models.DateTimeField(verbose_name='Дата создания')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('count_views', models.IntegerField(verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'ordering': ('title', 'creation_data', 'is_publish'),
            },
        ),
    ]