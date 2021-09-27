from datetime import datetime
from config import db, SQLAlchemyAutoSchema

class Previsao(db.Model):
    __tablename__ = 'previsao'
    id = db.Column(db.Integer, primary_key=True)
    data_execucao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    magnitude_verificada = db.Column(db.Numeric, nullable=False)
    magnitude_l_1 = db.Column(db.Numeric, nullable=False)
    magnitude_l_2 = db.Column(db.Numeric, nullable=False)
    magnitude_l_3 = db.Column(db.Numeric, nullable=False) 
    magnitude_l_4 = db.Column(db.Numeric, nullable=False) 
    magnitude_l_5 = db.Column(db.Numeric, nullable=False) 
    magnitude_l_6 = db.Column(db.Numeric, nullable=False) 
    magnitude_l_7 = db.Column(db.Numeric, nullable=False) 
    
    chuva_l_1 = db.Column(db.Numeric, nullable=False)
    chuva_l_2 = db.Column(db.Numeric, nullable=False)
    chuva_l_3 = db.Column(db.Numeric, nullable=False) 
    chuva_l_4 = db.Column(db.Numeric, nullable=False) 
    chuva_l_5 = db.Column(db.Numeric, nullable=False) 
    chuva_l_6 = db.Column(db.Numeric, nullable=False) 
    chuva_l_7 = db.Column(db.Numeric, nullable=False)

    direcao_l_1 = db.Column(db.Numeric, nullable=False)
    direcao_l_2 = db.Column(db.Numeric, nullable=False)
    direcao_l_3 = db.Column(db.Numeric, nullable=False)
    direcao_l_4 = db.Column(db.Numeric, nullable=False)
    direcao_l_5 = db.Column(db.Numeric, nullable=False)
    direcao_l_6 = db.Column(db.Numeric, nullable=False)
    direcao_l_7 = db.Column(db.Numeric, nullable=False)

    pressao_l_1 = db.Column(db.Numeric, nullable=False) 
    pressao_l_2 = db.Column(db.Numeric, nullable=False)
    pressao_l_3 = db.Column(db.Numeric, nullable=False)
    pressao_l_4 = db.Column(db.Numeric, nullable=False)
    pressao_l_5 = db.Column(db.Numeric, nullable=False)
    pressao_l_6 = db.Column(db.Numeric, nullable=False)
    pressao_l_7 = db.Column(db.Numeric, nullable=False)

    temperatura_l_1 = db.Column(db.Numeric, nullable=False)
    temperatura_l_2 = db.Column(db.Numeric, nullable=False)
    temperatura_l_3 = db.Column(db.Numeric, nullable=False)
    temperatura_l_4 = db.Column(db.Numeric, nullable=False)
    temperatura_l_5 = db.Column(db.Numeric, nullable=False)
    temperatura_l_6 = db.Column(db.Numeric, nullable=False)
    temperatura_l_7 = db.Column(db.Numeric, nullable=False)

    magnitude_d_1 = db.Column(db.Numeric, default=0, nullable=False)

# Serializador Objeto Python <-> Json
class PrevisaoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Previsao
        load_instance = True
        sqla_session = db.session