#!-*- coding: utf8 -*-
"""
   E este arquivo .py tem a finalidade de criar os modelos que seram persistidos no banco de dados.

    author: Ronaldo.Vasconcelos
"""
from django.db import models


class Planilha(models.Model):
    """ Classe que retonará os dados das processos por comarca e uf. """

    nome = models.CharField(verbose_name='Nome', max_length=80)
    cliente = models.CharField(verbose_name='Cliente', max_length=100)
    arquivo = models.FileField()

    class Meta:
        """ Formatação para exibição do admin do django """
        verbose_name = "Processo"
        verbose_name_plural = "Processos"
