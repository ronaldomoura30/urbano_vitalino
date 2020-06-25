#!-*- coding: utf8 -*-
"""
    Modulo core tem por finalidade administrar e redirecionar para outra telas do sistema e este
    arquivo .py é um repositorio de exceções customizadas .

    author: Ronaldo.Vasconcelos
"""


class FormatTypeArchiveException(Exception):
    """
        Classe customizada de exceção para tratar o formato do arquivo de conversao de pdf para
        excel
    """

    def __init__(self, archive: str):
        super().__init__()
        if archive:
            self._message = f"O arquivo passado {archive} precisa esta no formato PDF."
        else:
            self._message = f"O(s) arquivo(s) passado(s) precisa(m) estar no formato PDF."

    def __str__(self):
        return self._message
