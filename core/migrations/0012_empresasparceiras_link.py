# Generated by Django 3.2.15 on 2022-11-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_testemunhos_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresasparceiras',
            name='link',
            field=models.CharField(default='#', max_length=300, verbose_name='Link'),
            preserve_default=False,
        ),
    ]
