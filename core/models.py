from django.db import models
import uuid
from stdimage import StdImageField


def get_file_path(__instance, filename):
    ext = filename.split('.')[1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    service = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 580, 'height': 580, 'crop': True}})

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class ServicoAdicionais(Base):
    serviceAd = models.CharField('Serviço', max_length=100)
    descricaoAd = models.TextField('Descrição', max_length=500)
    imagemAd = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 580, 'height': 580, 'crop': True}})

    class Meta:
        verbose_name = 'Serviço Adicional'
        verbose_name_plural = 'Serviços Adicionais'

    def __str__(self):
        return self.serviceAd


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=500)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 580, 'height': 580, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class EmpresasParceiras(Base):
    empresa = models.CharField('Empresa', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 300, 'crop': True}})
    link = models.CharField('Link', max_length=300)
    
    class Meta:
        verbose_name = 'Empresa Parceia'
        verbose_name_plural = 'Empresas Parceiras'

    def __str__(self):
        return self.empresa


class Noticias(Base):
    manchete = models.CharField('Manchete', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 300, 'crop': True}})
    link = models.CharField('Link', max_length=300)

    class Meta:
        verbose_name = 'Manchete'
        verbose_name_plural = 'Manchetes'

    def __str__(self):
        return self.manchete


class Testemunhos(Base):
    ICONE_CHOICES = (
        ('fa-comments', 'Messege'),
    )
    depoimento = models.TextField('Depoimento', max_length=300)
    nome = models.CharField('Nome', max_length=100)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.depoimento
