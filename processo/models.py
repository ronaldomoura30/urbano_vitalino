#!-*- coding: utf8 -*-
"""
   E este arquivo .py tem a finalidade de criar os modelos que seram persistidos no banco de dados.

    author: Ronaldo.Vasconcelos
"""
from django.db import models


class Processo(models.Model):
    """ Classe que retonará os dados das processos por comarca e uf. """

    pasta = models.CharField(verbose_name='Pasta', max_length=100)
    comarca = models.CharField(verbose_name='Comarca', max_length=100)
    uf = models.CharField(verbose_name='UF', max_length=2)

    class Meta:
        """ Formatação para exibição do admin do django """
        verbose_name = "Processo"
        verbose_name_plural = "Processos"
        ordering = ['uf']
