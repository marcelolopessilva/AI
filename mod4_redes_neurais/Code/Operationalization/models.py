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
    temperatura_l_1 = db.Column(db.Numeric, nullable=False)
    temperatura_l_2 = db.Column(db.Numeric, nullable=False)
    temperatura_l_3 = db.Column(db.Numeric, nullable=False)
    direcao_l_1 = db.Column(db.Numeric, nullable=False)
    direcao_l_2 = db.Column(db.Numeric, nullable=False)
    direcao_l_3 = db.Column(db.Numeric, nullable=False)
    pressao_l_1 = db.Column(db.Numeric, nullable=False) 
    pressao_l_2 = db.Column(db.Numeric, nullable=False)
    pressao_l_3 = db.Column(db.Numeric, nullable=False)
    magnitude_d_1 = db.Column(db.Numeric, default=0, nullable=False)

# Serializador Objeto Python <-> Json
class PrevisaoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Previsao
        load_instance = True
        sqla_session = db.session