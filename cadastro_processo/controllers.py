#!-*- coding: utf8 -*-
"""
    Este arquivo .py tem a finalidade de executar operações e tratar dados para que
    sejam devolvidos para a view associada.

    author: Ronaldo Vasconcelos
"""
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from cadastro_processo.models import Planilha
from core.custom_exceptions import FormatTypeArchiveException
from processo.models import Processo


class CadastroProcessoController:
    """ Controlador de de Criação de Processos """
    def __init__(self, request, view, *args, **kwargs):
        """
            Inicialização do controlador.
            :param request: Requisição.
            :param view: View associada.
            :param args: args da view.
            :param kwargs: kwargs da view.
        """
        self._request = request
        self._view = view
        self._args = args
        self.kwargs = kwargs
        self._nome = request.POST.get("nome")
        self._cliente = request.POST.get("cliente")
        self._arquivo = request.FILES['arquivo']
        self._message = "O arquivo foi salvo com sucesso."

    def __str__(self):
        """
            Retorna a mensagem referente à execução.
            :return: Instância do controlador.
        """
        return self._message

    def execute(self):
        """
            Executa a criação dos grupos.
            :return: Instância do controlador
        """
        arquivo_carregado = self._arquivo

        if not arquivo_carregado.content_type == "text/csv":
            raise FormatTypeArchiveException(arquivo_carregado.name)

        self._save_processo(arquivo=arquivo_carregado)

        return self

    def _save_processo(self, arquivo):
        """
            Salva os dados do grupo.
            :param desc: Descrição do grupo.
            :return: Instância do controlador.
        """
        # Classe que irá armazenar o arquivo convertidos usando recursos nativa do django
        path = f"{settings.MEDIA_ROOT}/planilhas"
        fs = FileSystemStorage(location=path)

        # Salvando o arquivo
        nome_arquivo = fs.save(name=arquivo.name, content=arquivo)
        caminho = f"{path}/{nome_arquivo}"

        if os.path.exists(caminho):
            with open(caminho, 'r') as var:
                for index, registro in enumerate(var):
                    if not index == 0:
                        pasta, comarca, uf = registro.replace("\n", "").split(";")
                        processo = Processo(pasta=pasta, comarca=comarca, uf=uf)
                        processo.save()

        planilha = Planilha(nome=self._nome, cliente=self._cliente, arquivo=caminho)
        planilha.save()

        return self