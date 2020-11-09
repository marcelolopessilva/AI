
# Relatório de Dados

Esse relatório das bases de dados do projeto.


## Bases de dados


| Nome Dataset | Origem   | Destino  | Script |
| ---:| ---: | ---: | ---: | -----: |
| Comentários| Comentários e sentimentos | Processado para qualidade de dados | [data_prep.ipynb](../../Code/DataPrep/data_perp.ipynb) | 


* Base de Comentários
Possui somente duas colunas: 'class' e 'text'. A coluna com a classe, ou o sentimento do comentário, possui os valores *Neg* e *Pos*. Cada classe possui 1000 comentários de textos.

Os textos dos comentários são strings de 92 a 14.958 caracteres. Em média, cada comentário tem comprimento de 3.894 caracteres.

Não foram encontrados valores nulos na base de dados.




