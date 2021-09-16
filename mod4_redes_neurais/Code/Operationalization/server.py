from models import Previsao
from flask import render_template
from sqlalchemy import desc
import config

app = config.connex_app

# Lê arquivo swagger.yml para configurar os endpoints da api
app.add_api("swagger.yml")

@app.route('/')
def index():
    """
    Essa função responde a requisição localhost:5000/
    :return:        O template renderizado "index.html"
    """
    # Recupera do banco de dados todas as previsões ordenadas por data
    previsoes = Previsao.query.order_by(desc(Previsao.data_execucao)).all()
    # Retorna a renderização de index.html 
    return render_template('index.html', previsoes=previsoes)

if __name__ == "__main__":
    app.run(debug=True)
