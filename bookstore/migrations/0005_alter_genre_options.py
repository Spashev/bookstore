# Generated by Django 3.2.8 on 2022-01-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_book_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
    ]
