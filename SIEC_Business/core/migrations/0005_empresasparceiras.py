# Generated by Django 3.2.15 on 2022-09-10 18:58

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_funcionario_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresasParceiras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 126, 'width': 270}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Empresa Parceia',
                'verbose_name_plural': 'Empresas Parceiras',
            },
        ),
    ]
