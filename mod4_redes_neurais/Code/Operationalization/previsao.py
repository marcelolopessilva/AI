"""
O módulo provisao.py dá suporte para todas as ações REST dos dados de previsão 
"""

from flask import make_response, abort
from config import db
from models import Previsao, PrevisaoSchema

def criar(previsao):
    """
    Essa função cria uma nova permissão baseada nos dados de previsão recebido no POST
    :param previsao:  Previsao a ser criada
    :return:        201 sucesso
    """

    schema = PrevisaoSchema()
    nova_previsao = schema.load(previsao, session=db.session)

    # Adiciona a previsão no banco de dados
    db.session.add(nova_previsao)
    db.session.commit()

    # Serializa o obj python em json e retorna como resposta do request
    data = schema.dump(nova_previsao)

    return data, 201