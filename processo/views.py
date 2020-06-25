# coding=utf-8
""" E este arquivo .py tem uma das finalidades a exibição desses dados na tela

    author: Ronaldo.Vasconcelos
"""
from django.views.generic import ListView
from .models import Processo


class IndexView(ListView):

    model = Processo
    template_name = 'processo/processo_list.html'
    context_object_name = 'object_list'
    paginate_by = 6

    def get_queryset(self):
        """
            Função responsavel por consultar todos os processos cadastrados
        """
        return Processo.objects.all()

    """ Classe herdada do generic view do Django para exibição da tela principal do portal """


