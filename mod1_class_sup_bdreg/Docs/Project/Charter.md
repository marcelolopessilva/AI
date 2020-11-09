# Project Charter

## Entendimento de negócio

A Base de Dados de Regulação (DBREG) é um sistema que guarda informações de atos regulatórios do Governo Brasileiro, classificadas como "de interesse", para a empresa contratante. Estas informações são disponibilizadas em categorias nas edições diárias do Diário Oficial ([DOU](https://www.in.gov.br/web/guest/inicio) e classificadas por pessoas qualificadas como "de interesse" no contexto do Setor Elétrico. 

Um trabalho adicional deverá ser feito para de forma que as informações que não são de interesse sejam agregadas a uma base única. Desta forma tenta-se evitar vício na classificação automatizada. 

Diariamente, até as 10:00am, as informações dos atos regulatórios do DOU devem ser classificadas. Atualmente a quantidade de analistas não permite que a classificação com esta restrição possa ser realizada. Em média são 250 atos ou portarias por dia e o diário oficial é disponibilizado por volta de 8:00am. 
O uso de machine learning permitirá uma classificação prévia automática que poderá ser rapidamente confirmada pelos analistas, reduzindo o tempo do processo e garantindo feedback para retreino do modelo quando necessário. 

## Escopo

O problema de análise de importância pode ser abordado como um problema de classificação. Como a base inicial já estará avaliadas previamente, trata-se de um problema para algoritmos de treinamento supervisionado. A quantidade de possíveis valores para a classe a alvo indica que é um problema de classificação binária (de interesse ou sem interesse).

* **Problema**: classificação binária
* **Algoritmo**: treinamento supervisionado
* **Base de dados**: arquivo csv com informações de texto livre gerado a partir da base de dados do BDREG e [site](https://inlabs.in.gov.br/acessar.php) com arquivos em formato xml que disponibiliza arquivos no formato xml com todas as seções do DOU.
* **Variável alvo**: Classe "Interesse", "Sem Interesse"

## Métricas
* Objetivo qualitativo: estimar importância de regulações do DOU para a empresa contratante.
* Figura de mérito: f1-score.
* Benchmarking: melhor que o aleatório de 50%.
* Métrica deve ser medida sobre um conjunto de teste de pelo menos 20% dos dados para cada classe.


## Planejamento
* Sprint 1: entendimento de negócio e preparação dos dados.
* Sprint 2: Análise de dados e construção de features.
* Sprint 3: Modelagem dos classificadores e avaliação dos resultados
* Sprint 4: Relatório dos resultados do modelo

## Arquitetura

* Dados:
  * Os dados são entregues através de 1 arquivo CSV com a base de interesse e vários arquivos xml
  * Relatório de dados disponível [aqui](../DataReport/Report.md "Relatório de dados")

* Modelos:
  * Classificador binário para estimar a probabilidade do comentário ser relevante.
  * Serão utilizados modelos lineares como: AdaBoost, NaiveBayes, Regressão Logística, DecisionTree.
  * Será utilizado um modelos não-lineares: RandomForest.
  * Os hiper-parâmetros dos modelos serão ajustados segundo uma busca exaustiva em grid-search.
  * A base de dados será dividida em treino (80%) e teste (20%), mantendo a proporção de classes nos dois conjuntos de dados.
  * Os modelos serão avaliados considerando o conjunto de teste.
  * Os modelos e as análises sobre os dados podem ser estudadas [aqui](../Model/Report.md "Relatório de modelagem")
 
* Entregáveis:
  * Apresentação com os resultados mais relevantes.
  * Modelo de classificação "melhor avaliado" para uso em novas classificações.
  * Estrutura operacional com:
    * Processo automatizado de extração de informações do diário oficial
    * API REST com consulta de informações do diário oficial
    * API REST MaS (Model as a Service) com funcionalidades de classificação e retreino de modelo
    * Python Notebooks com processos de preparação de dados, análises e modelagem

## Comunicação
* Equipe de desenvolvimento com reuniões a cada 2 dias em modelo Scrum.
* Reuniões de status executivos a cada 1 semana.
* Pontos de contato:
  * Empresa: Analistas e Gerente
  * Consultoria: Analistas de Data Science
