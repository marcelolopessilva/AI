# Project Charter

## Entendimento de negócio

O IMDb é um portal online para avaliação de filmes por espectadores do mundo todo. A avaliação é através da nota e "estrelas" que um filme tem. O projeto consiste em utilizar os comentários dos filmes para estimar o sentimento dos espectadores.

A construção da base de dados considerou somente os sentimentos classificados como *Positivo*(**pos**) ou *Negativo*(**neg**) de acordo com a nota/estrela dada pelo espectador. 

Deseja-se utilizar a informação dos comentários escritos nas avaliações para prever o sentimento do avaliador pelo filme (**pos** ou **neg**). A mesma solução desenvolvida poderia, por exemplo, ser utilizada para estimar o sentimento dos usuários de Twitter em relação aos filmes em cartaz, direcionamento campanhas de marketing e afins.


## Escopo

O problema de análise de sentimento pode ser abordado como um problema de classificação. Como as bases já estão avaliadas previamente, trata-se de um problema para algoritmos de treinamento supervisionado. A quantidade de possíveis valores para as classes indica que é um problema de classificação binária.

* **Problema**: classificação binária
* **Algoritmo**: treinamento supervisionado
* **Base de dados**: arquivo csv com comentários de texto livre
* **Variável alvo**: Sentimento positivo ou negativo

## Métricas
* Objetivo qualitativo: estimar o sentimento de comentários sobre filmes.
* Figura de mérito: f1-score.
* Benchmarking: melhor que o aleatório de 50%.
* Métrica deve ser medida sobre um conjunto de teste de 20% dos dados para cada classe.


## Planejamento
* Sprint 1: entendimento de negócio e preparação dos dados.
* Sprint 2: Análise de dados e construção de features.
* Sprint 3: Modelagem dos classificadores e avaliação dos resultados
* Sprint 4: Relatório dos resultados do modelo

## Arquitetura

* Dados:
  * Os dados são entregues através de 1 arquivo CSV
  * Relatório de dados disponível [aqui](../DataReport/Report.md "Relatório de dados")

* Modelos:
  * Classificador binário para estimar a probabilidade do comentário ter sentimento positivo.
  * Será utilizado um modelo linear de Regressão Logística.
  * Serão utilizados três modelos não-lineares: RandomForest, SVM e o kNN.
  * Os hiper-parâmetros dos modelos serão ajustados segundo uma busca exaustiva em grid-search.
  * A base de dados será dividida em treino (80%) e teste (20%), mantendo a proporção de classes nos dois conjuntos de dados.
  * Os modelos serão avaliados considerando o conjunto de teste.
  * Os modelos e as análises sobre os dados podem ser estudadas [aqui](../Model/Report.md "Relatório de modelagem")
  
  
* Entregáveis:
  * Apresentação com os resultados mais relevantes.
  * Base de dados de teste com a probabilidade de sentimento positivo dos comentários, em arquivo Excel.


