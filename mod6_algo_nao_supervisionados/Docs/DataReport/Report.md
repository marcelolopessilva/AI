
# Relatório de Dados

Apresenta as bases de dados do projeto. 

## Bases de dados

|Nome Dataset|Origem|Destino|Script|
| :---:| ---: | ---: | ---: |
informacao.csv|Base de Dados - ONS|Pasta Data/Raw|[Data Preparation](../../Code/DataPrep/Data%20Preparation%20-%20Household%20comsumption.ipynb)|
topico_informacao.csv|Base de Dados - ONS|Pasta Data/Raw|[Data Preparation](../../Code/DataPrep/Data%20Preparation%20-%20Household%20comsumption.ipynb)|
topico.csv|Base de Dados - ONS|Pasta Data/Raw|[Data Preparation](../../Code/DataPrep/Data%20Preparation%20-%20Household%20comsumption.ipynb)|
</br>

<b>informacao.csv</b> - Apresenta o seguinte formato

| Nome Coluna | Descrição |
| ---:| ---: |
id_informacao| Identificador da informação no banco de dados
dsc_objeto| Título do objeto extraído e classificado do DOU
dsc_informacao| Texto do objeto relevante extraído e classificado do DOU
lgn_inclusao| Login do usuário que incluíu o texto no sistema
din_inclusao| Data da inclusão do texto no formato yyyy-mm-dd hh24:mi:ss:ms
din_primeiradivulgacao| Data da primeira inclusão do texto no formato yyyy-mm-dd hh24:mi:ss:ms
din_ultimadivulgacao| Data da última inclusão do texto no formato yyyy-mm-dd hh24:mi:ss:ms

<b>topico_informacao.csv</b> - Apresenta o seguinte formato

| Nome Coluna | Descrição |
| ---:| ---: |
id_informacao| Identificador da informação no banco de dados
id_topico| Identificador do tópico no banco de dados

<b>topico.csv</b> - Apresenta o seguinte formato

| Nome Coluna | Descrição |
| ---:| ---: |
id_topico| Identificador do tópico no banco de dados
nom_topico| Nome do tópico no banco de dados 