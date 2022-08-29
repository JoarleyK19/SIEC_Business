from django.db import models

# from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = models.ImageField(upload_to='service')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


# class Cargo(Base):
#     cargo = models.CharField('Cargo', max_length=100)
#
#     class Meta:
#         verbose_name = 'Cargo'
#         verbose_name_plural = 'Cargos'
#
#     def __str__(self):
#         return self.cargo
#
#
# class Funcionario(Base):
#     nome = models.CharField('Nome', max_length=100)
#     cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE())
#     bio = models.TextField('Bio', max_length=200)
#     imagem = StdImageField('Imagem', upload_to='service', variations={'tumb': {'width': 480, 'heigth': 480, 'crop': True}})
