# Generated by Django 3.2.15 on 2022-10-27 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_noticia_news_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='titulo',
            new_name='noticias',
        ),
    ]
