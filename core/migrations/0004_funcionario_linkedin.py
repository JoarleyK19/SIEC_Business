# Generated by Django 3.2.15 on 2022-09-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cargo_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='linkedin',
            field=models.CharField(default='#', max_length=100, verbose_name='Linkedin'),
        ),
    ]