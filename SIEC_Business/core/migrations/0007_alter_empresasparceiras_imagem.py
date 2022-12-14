# Generated by Django 3.2.15 on 2022-09-10 19:10

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_image_empresasparceiras_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresasparceiras',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 300, 'width': 300}}, verbose_name='Imagem'),
        ),
    ]
