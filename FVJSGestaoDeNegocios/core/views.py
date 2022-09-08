from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, ServicoAdicionais
from .form import ContatoForm


class IndexView(TemplateView):
    template_name = 'index.html'


class FormsView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(FormsView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(FormsView, self).form_invalid(form, *args, **kwargs)


class ServiceView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        contex = super(ServiceView, self).get_context_data(**kwargs)
        contex['service'] = Servico.objects.all()
        contex['serviceAd'] = ServicoAdicionais.objects.all()
        return contex


class SobrenosView(TemplateView):
    template_name = 'sobrenos.html'


class EmpresasView(TemplateView):
    template_name = 'empresas.html'


class PoliticasView(TemplateView):
    template_name = 'politicas.html'
