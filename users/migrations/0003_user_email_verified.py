# Generated by Django 4.2.6 on 2023-11-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_avatar_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Верификация почты'),
        ),
    ]
