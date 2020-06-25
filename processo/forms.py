#!-*- coding: utf8 -*-
"""
    Este arquivo .py tem é o formulario personalizado para criação de um processo sendo
    possível também usar o email para acessar o portal

    author: Ronaldo.Vasconcelos
"""
from django import forms

from .models import Processo


class ProcessoForm(forms.ModelForm):
    """ Classe que renderiza um formulário do objeto processo """

    class Meta:
        """ Classe de metadata para o formulario ProcessoForm """

        model = Processo
        fields = ("pasta", "comarca", "uf")
        widgets = {
            'uf': forms.Select(attrs={"name": "uf"})}
