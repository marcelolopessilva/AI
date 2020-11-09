from .settings import PATH_MODELO_TREINADO

import joblib

model_file = PATH_MODELO_TREINADO + 'modelo_treinado_dou.jbl'

# Loading models at the service initialization
if 'globalTrainResults' not in dir():
    print('Carregando modelos de ', model_file)
    globalTrainResults = joblib.load(model_file)