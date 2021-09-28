"""
O módulo provisao.py dá suporte para todas as ações REST dos dados de previsão 
"""

from flask import make_response, abort
from config import db
from models import Previsao, PrevisaoSchema
from config import nn_model, x_scaler, y_scaler
import numpy as np

def criar(previsao):
    """
    Essa função cria uma nova permissão baseada nos dados de previsão recebido no POST
    :param previsao:  Previsao a ser criada
    :return:        201 sucesso
    """

    # Transforma dicionário de entrada http post em numpy array utilizado pelo modelo
    previsao_np_array = np.fromiter(previsao.values(), dtype = float, count=36)
    previsao_np_array = previsao_np_array.reshape(-1,1)

    # Normaliza entrada com x_scaler utilizado no treino do modelo
    previsao_np_array_scaler = x_scaler.fit_transform(previsao_np_array)  

    # Utiliza o modelo para prever a magnitude do vento da próxima hora, desnormalizando o resultado
    magnitude_estimada  = y_scaler.inverse_transform(nn_model.predict(np.array([previsao_np_array_scaler])))

    previsao['magnitude_d_1'] = magnitude_estimada[0][0]

    schema = PrevisaoSchema()

    nova_previsao = schema.load(previsao, session=db.session)

    # Adiciona a previsão no banco de dados
    db.session.add(nova_previsao)
    db.session.commit()

    # Serializa o obj python em json e retorna como resposta do request
    data = schema.dump(nova_previsao)

    return data, 201