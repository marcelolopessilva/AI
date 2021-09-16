import os
from config import db
from models import Previsao

# Dados para inicializar o banco de dados. Teste somente. Comentar antes do golive
PREVISAO = [
    {'magnitude_verificada': 8.0,'magnitude_l_1': 8.3, 'magnitude_l_2': 7.9,'magnitude_l_3': 8.5,
    'temperatura_l_1': 24.3, 'temperatura_l_2': 25.4,'temperatura_l_3': 26.0,
    'direcao_l_1': 68, 'direcao_l_2': 45,'direcao_l_3': 55,
    'pressao_l_1': 1013.3, 'pressao_l_2': 1012.0,'pressao_l_3': 1014.9, 'magnitude_d_1': 9.0},
    {'magnitude_verificada': 9.0, 'magnitude_l_1': 9.2, 'magnitude_l_2': 10.5,'magnitude_l_3': 12.3,
    'temperatura_l_1': 28.1, 'temperatura_l_2': 32.3,'temperatura_l_3': 27.2,
    'direcao_l_1': 104, 'direcao_l_2': 125,'direcao_l_3': 141,
    'pressao_l_1': 1008.1, 'pressao_l_2': 1010.0,'pressao_l_3': 1009.2, 'magnitude_d_1':10.2},
]

# Apaga o database se ele já existir
if os.path.exists('prev_ventos.db'):
    os.remove('prev_ventos.db')

# Cria o database
db.create_all()

# Popula o database com os dados dummy
#for previsao in PREVISAO:
#    p = Previsao(magnitude_verificada=previsao['magnitude_verificada'], 
#                magnitude_l_1=previsao['magnitude_l_1'], magnitude_l_2=previsao['magnitude_l_2'], magnitude_l_3=previsao['magnitude_l_3'],
#                temperatura_l_1=previsao['temperatura_l_1'], temperatura_l_2=previsao['temperatura_l_2'], temperatura_l_3=previsao['temperatura_l_3'],
#                direcao_l_1=previsao['direcao_l_1'], direcao_l_2=previsao['direcao_l_2'], direcao_l_3=previsao['direcao_l_3'],
#                pressao_l_1=previsao['pressao_l_1'], pressao_l_2=previsao['pressao_l_2'], pressao_l_3=previsao['pressao_l_3'],
#                magnitude_d_1=previsao['magnitude_d_1'])
#    db.session.add(p)

db.session.commit()