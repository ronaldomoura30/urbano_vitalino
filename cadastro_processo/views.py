#!-*- coding: utf8 -*-
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.custom_exceptions import FormatTypeArchiveException
from .models import Planilha
from .forms import PlanilhaForm
from .controllers import CadastroProcessoController


class CadastroProcessoView(CreateView):
    """ Classe de criação de processos """

    model = Planilha
    form_class = PlanilhaForm
    template_name = 'cadastro_processo/processo_create.html'
    success_url = reverse_lazy('processo:index')

    def get_form_class(self):
        """ Retornar o formulario do processo """
        return self.form_class

    def post(self, request, *args, **kwargs):
        """
            Função que recebe o nome do grupo, a campanha ao qual o grupo esta associado e a
            quantidade de grupos quer criar indicando um número inicial para o título do grupo.
        """
        try:
            messages.success(request, CadastroProcessoController(request=request, view=self, *args,
                                                                 **kwargs).execute())
        except FormatTypeArchiveException as format_erro:
            messages.error(request, format_erro)
            return render(request, self.template_name, {'form': self.get_form()})
        except Exception as ex:
            messages.error(request, ex)
            return render(request, self.template_name, {'form': self.get_form()})

        return redirect(self.success_url)


cadastro_processo = CadastroProcessoView.as_view()

