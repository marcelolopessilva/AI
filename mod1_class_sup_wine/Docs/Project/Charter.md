# Project Vivino AI

## Entendimento de negócio

Um importador de vinhos portugueses deseja aumentar o lucro de suas vendas. Para manter o interesse de seus clientes, e dada a grande variedade de produtores de vinhos em Portugal, ele sempre está realizando a compra de novos vinhos. Nem sempre os vinhos caem no gosto dos clientes, independente de serem caros ou baratos. O importador gostaria de classificar os vinhos que compra entre duas classes: baixa e alta qualidade de acordo com as características de cada vinho.
Os produtores portugueses provém várias informações que caracterizam seu vinho, como: acidez, teor alcoólico, pH, densidade, sulfatos e outros.

## Escopo

A empresa gostaria de investir numa solução baseada em dados para auxiliar os consultores da empresa em suas decisões de planejamento de compras e vendas. Para isso, a empresa utilizou uma base histórica em conjunto com um grupo de variáveis que são consideradas interessantes para o entendimento do volume de vendas e consequentemente seu lucro.

* A solução deve observar o histórico de dados e prover uma avaliação, por nota de qualidade para cada vinho
* Os dados serão coletadas através de arquivos CSV.
* O resultado da previsão será exportado como arquivo CSV.
* O resultado pode ser consumido em relatórios estáticos.

## Pessoal
* Quem está no projeto:
	* Consultoria:
		* Project lead (Marcelo Lopes)
		* PO (Marcelo Lopes)
		* Data scientist(s) (Marcelo Lopes)
		* Account manager (Marcelo Lopes)
	* Vivino:
		* Data administrator (Maria José)
		* Business contact (Anderson)

## Métricas
* Objetivo qualitativo: Acurácia igual ou superior a 80%. Quantidade de acertos de avaliação por quantidade de existentes
* Figura de mérito: f1-socore
* Benchmarking: processo atual é subjetivo e conta com a classificação de vinhos realizada por enólogos da empresa.
* Métrica deve ser medida sobre todo o histórico de teste.


## Planejamento
O projeto deve ser realizado em 1 mes. Está prevista a passagem de conhecimento entre os especialistas do negócio e a equipe de cientistas de dados (representada pelo PO).

* Conhecimento dos dados - Entendimento do negócio e o contexto em que os dados e informaçẽos se inserem. Planejamento e desenho da solução.
* Pré Processamento - Adequação/Formatação dos dados, Tratamento de dados faltantes e forma da curva, criação/exclusão de variáveis, redução de dimensionalidade se for o caso
* Escolha e aplicação do modelo de machine learning
* medição dos resultados
* Aperfeiçoamento
* Geração de relatórios e documentação e apresentação dos resultados finais e transferência de conhecimento.

## Arquitetura

* Dados:
  * Os dados são entregues através de 2 arquivos CSV, um para vinhos tintos e outro para vinhos brancos, entregues por uma empresa especializada em pesquisas. Os dados coletados são processados para saneamento e avaliação da sua qualidade.
  * A série histórica possui aproximadamente 7000 registros.
  * São coletadas 12 variáveis exógenas.

* Modelos:
  * Serão avlaidos os modelos de regressão logística, árvore de decisões e knn para a previsão da qualidade dos vinhos.
  * Os modelos serão desenvolvidos utilizando jupyter notebooks.

* Relatórios:
  * Os relatórios serão feitos após o processamento do treinamento dos modelos.
  * Os relatórios são disponibilizados como exportações HTML dos notebooks utilizados.

## Comunicação
* Equipe de desenvolvimento com reuniões diárias em modelo Scrum.
* Reuniões de status executivos a cada semana.
* Pontos de contato:
  * Vivino Co.: Anderson 
  * Consultoria: Marcelo Lopes
