#!-*- coding: utf8 -*-
"""
    Este arquivo .py tem é o formulario personalizado para criação de um usuário sendo
    possível também usar o email para acessar o portal

    author: Ronaldo.Vasconcelos
"""
from django import forms

from cadastro_processo.models import Planilha


class PlanilhaForm(forms.ModelForm):
    """ Classe que renderiza um formulário do objeto planilha """

    class Meta:
        """ Classe de metadata para o formulario PlanilhaForm """

        model = Planilha
        fields = ('nome', 'cliente', 'arquivo')
