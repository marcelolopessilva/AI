# ![logo_infnet](infnet.png)  MIT_Data_Science

## Trabalho do módulo PGPIAL01C2-3N-P1 - Validação de modelos de clusterização
<br />

### Professor: [Fernando Guimarães Ferreirea](mailto:Fernando.gFerreira@infnet.edu.br)
<br />

# Descrição do Problema

Tentar identificar assuntos em comum, ex.: tópicos, em textos do Diário Oficial da União - [DOU](https://www.gov.br/imprensanacional/pt-br) pré selecionados por relevância pelo Operador Nacional do Sistema Elétrico - [ONS](http://www.ons.org.br).

## Contexto

O ONS seleciona de forma automática com o uso de IA, textos do DOU de interesse ao Operador. Essa seleção é feita por um classificador treinado de forma supervisionada e posteriormente são associados tópicos manualmente aos textos. Pode ser associado mais de um tópico por texto. A ideia inicial é identificar esse tópicos de forma não supervisionada e com a experiência adquirida partir para a criação de um identificador de tópicos para novos textos.

## Características do Data Set
Textual, Sem dependência temporal.

## Tarefas Associadas
Clusterização não supervisionada, Processamento em Linguagem Natural

## Informações do Data Set e seus atributos:

Ver em [Data Report](./DataReport/Report.md)

<br>

# Como usar

Todo o código foi desenvolvido em Python 3.10.1 em ambiente windows 11

Todas as dependências foram instaladas utilizando a ferramenta [pipenv](https://pypi.org/project/pipenv/) versão 2021.11.23

* Siga as instruções do link acima para instalar o pipenv
* Para instalar as dependências deste projeto use:$ pipenv install --dev

### Dependências necessárias



## 2 - Relatório de Dados

Em Docs/DataReport pode ser encontrado o relatório de dados do projeto [Relatório de dados](./DataReport/Report.md).

## 3 - Preparação de Dados

Em Code/DataPrep existe o notebook [DataPreparation](../Code/DataPrep/Data%20Preparation%20-%20Household%20comsumption.ipynb). Este notebook é reponsável pela preparação dos dados: limpeza, conformidade e criação de características para que os dados possam ser utilizados pelos 

## 4 - Análise Exploratória de Dados

Em Code/Analysis existe o notebook [DataAnalysisExploration](../Code/Analysis/Data%20Analysis%20-%20Exploratory%20Data%20Analysis.ipynb). Neste notebook encontra-se a análise exploratória de dados responsável pelo melhor entendimento das informações do projeto.

## 5 - Modelagem

Em Code/Model existe o notebook [DataModeling](../Code/Model/Model%20-%20Clusterization.ipynb). Neste notebook são aplicadas técnicas de normalização de dados, clusterização e validações de qualidade de dados. 
