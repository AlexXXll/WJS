# Generated by Django 3.1.2 on 2020-11-18 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201115_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='taskimage',
            options={'verbose_name': 'Фотография поста', 'verbose_name_plural': 'Фотографии поста'},
        ),
    ]
