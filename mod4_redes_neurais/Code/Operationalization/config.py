import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

'''
EndPoints
http://127.0.0.1:5000/api/ui/       (GET) - Documentação API
http://127.0.0.1:5000/              (GET) - Base index.html
http://127.0.0.1:5000/api/previsao  (POST) - Criar Previsão
'''

basedir = os.path.abspath(os.path.dirname(__file__))

# Cria uma instância da aplicação Connexion - https://connexion.readthedocs.io/en/latest/
connex_app = connexion.FlaskApp(__name__, specification_dir=basedir)

# Recupera a instância da Flask app
app = connex_app.app

# Configura o SQLAlchemy na instancia da app
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'prev_ventos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria a instância db do SQLAlchemy
db = SQLAlchemy(app)