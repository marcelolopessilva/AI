# ![logo_infnet](infnet.png)  MIT_Data_Science

## Trabalho do módulo PGPIAL01C2-3N-P1 - Algoritmos Não-Supervisionados para clusterização
<br />

### Professor: [Anderson Cordeiro](https://github.com/andersoncordeiro)
<br />

# Descrição do Problema

[kaggle link](https://www.kaggle.com/uciml/electric-power-consumption-data-set)

I need help to analyze this data set with R code, if someone can help me I'd appreciate a lot and I'd send some money for his kindness. I really need how to do a regression and clustering manipulating this data.
Sorry about the format, it's in text file.
Thanks in advance :)

## Context

Measurements of electric power consumption in one household with a one-minute sampling rate over a period of almost 4 years. Different electrical quantities and some sub-metering values are available.

## Data Set Characteristics
Multivariate, Time-Series

## Associated Tasks
Regression, Clustering

## Data Set Information:

This archive contains 2.075.259 measurements gathered between December 2006 and November 2010 (47 months).

Notes:

1. globalactivepower*1000/60 - submetering1 - submetering2 - submetering3 represents the active energy consumed every minute (in watt hour) in the household by electrical equipment not measured in sub-meterings 1, 2 and 3.

2. The dataset contains some missing values in the measurements (nearly 1,25% of the rows). All calendar timestamps are present in the dataset but for some timestamps, the measurement values are missing: a missing value is represented by the absence of value between two consecutive semi-colon attribute separators. For instance, the dataset shows missing values on April 28, 2007.

## Attribute Information

1. **date**: Date in format dd/mm/yyyy

2. **time**: time in format hh:mm:ss

3. **globalactivepower**: household global minute-averaged active power (in kilowatt)

4. **globalreactivepower**: household global minute-averaged reactive power (in kilowatt)

5. **voltage**: minute-averaged voltage (in volt)

6. **global_intensity**: household global minute-averaged current intensity (in ampere)

7. **submetering1**: energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered).

8. **submetering2**: energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light.

9. **submetering3**: energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.
<br />
<br />

# Como usar

Todo o código foi desenvolvido em Python 3.10.1 em ambiente windows 11

Todas as dependências foram instaladas utilizando a ferramenta [pipenv](https://pypi.org/project/pipenv/) versão 2021.11.23

* Siga as instruções do link acima para instalar o pipenv
* Para instalar as dependências deste projeto use:$ pipenv install --dev

### Dependências necessárias

cramjam==2.5.0
fsspec==2021.11.1
ipykernel==6.6.0
  - debugpy [required: >=1.0.0,<2.0, installed: 1.5.1]
  - ipython [required: >=7.23.1, installed: 7.30.1]
    - backcall [required: Any, installed: 0.2.0]
    - colorama [required: Any, installed: 0.4.4]
    - decorator [required: Any, installed: 5.1.0]
    - jedi [required: >=0.16, installed: 0.18.1]
      - parso [required: >=0.8.0,<0.9.0, installed: 0.8.3]
    - matplotlib-inline [required: Any, installed: 0.1.3]
      - traitlets [required: Any, installed: 5.1.1]
    - pickleshare [required: Any, installed: 0.7.5]
    - prompt-toolkit [required: >=2.0.0,<3.1.0,!=3.0.1,!=3.0.0, installed: 3.0.24]
      - wcwidth [required: Any, installed: 0.2.5]
    - pygments [required: Any, installed: 2.10.0]
    - setuptools [required: >=18.5, installed: 58.3.0]
    - traitlets [required: >=4.2, installed: 5.1.1]
  - jupyter-client [required: <8.0, installed: 7.1.0]
    - entrypoints [required: Any, installed: 0.3]
    - jupyter-core [required: >=4.6.0, installed: 4.9.1]
      - pywin32 [required: >=1.0, installed: 303]
      - traitlets [required: Any, installed: 5.1.1]
    - nest-asyncio [required: >=1.5, installed: 1.5.4]
    - python-dateutil [required: >=2.1, installed: 2.8.2]
      - six [required: >=1.5, installed: 1.16.0]
    - pyzmq [required: >=13, installed: 22.3.0]
    - tornado [required: >=4.1, installed: 6.1]
    - traitlets [required: Any, installed: 5.1.1]
  - matplotlib-inline [required: >=0.1.0,<0.2.0, installed: 0.1.3]
    - traitlets [required: Any, installed: 5.1.1]
  - tornado [required: >=4.2,<7.0, installed: 6.1]
  - traitlets [required: >=5.1.0,<6.0, installed: 5.1.1]
nbformat==5.1.3
  - ipython-genutils [required: Any, installed: 0.2.0]
  - jsonschema [required: >=2.4,!=2.5.0, installed: 4.3.3]
    - attrs [required: >=17.4.0, installed: 21.4.0]
    - pyrsistent [required: >=0.14.0,!=0.17.2,!=0.17.1,!=0.17.0, installed: 0.18.0]
  - jupyter-core [required: Any, installed: 4.9.1]
    - pywin32 [required: >=1.0, installed: 303]
    - traitlets [required: Any, installed: 5.1.1]
  - traitlets [required: >=4.1, installed: 5.1.1]
plotly==5.5.0
  - six [required: Any, installed: 1.16.0]
  - tenacity [required: >=6.2.0, installed: 8.0.1]
seaborn==0.11.2
  - matplotlib [required: >=2.2, installed: 3.5.1]
    - cycler [required: >=0.10, installed: 0.11.0]
    - fonttools [required: >=4.22.0, installed: 4.28.5]
    - kiwisolver [required: >=1.0.1, installed: 1.3.2]
    - numpy [required: >=1.17, installed: 1.22.0]
    - packaging [required: >=20.0, installed: 21.3]
      - pyparsing [required: >=2.0.2,!=3.0.5, installed: 3.0.6]
    - pillow [required: >=6.2.0, installed: 9.0.0]
    - pyparsing [required: >=2.2.1, installed: 3.0.6]
    - python-dateutil [required: >=2.7, installed: 2.8.2]
      - six [required: >=1.5, installed: 1.16.0]
  - numpy [required: >=1.15, installed: 1.22.0]
  - pandas [required: >=0.23, installed: 1.3.5]
    - numpy [required: >=1.21.0, installed: 1.22.0]
    - python-dateutil [required: >=2.7.3, installed: 2.8.2]
      - six [required: >=1.5, installed: 1.16.0]
    - pytz [required: >=2017.3, installed: 2021.3]
  - scipy [required: >=1.0, installed: 1.7.3]
    - numpy [required: >=1.16.5,<1.23.0, installed: 1.22.0]
sklearn==0.0
  - scikit-learn [required: Any, installed: 1.0.2]
    - joblib [required: >=0.11, installed: 1.1.0]
    - numpy [required: >=1.14.6, installed: 1.22.0]
    - scipy [required: >=1.1.0, installed: 1.7.3]
      - numpy [required: >=1.16.5,<1.23.0, installed: 1.22.0]
    - threadpoolctl [required: >=2.0.0, installed: 3.0.0]
thrift==0.15.0
  - six [required: >=1.7.2, installed: 1.16.0]

## 2 - Relatório de Dados

Em Docs/DataReport pode ser encontrado o relatório de dados do projeto [Relatório de dados](./DataReport/Report.md).

## 3 - Preparação de Dados

Em Code/DataPrep existe o notebook [DataPreparation](../Code/DataPrep/Data%20Preparation%20-%20Household%20comsumption.ipynb). Este notebook é reponsável pela preparação dos dados: limpeza, conformidade e criação de características para que os dados possam ser utilizados pelos 

## 4 - Análise Exploratória de Dados

Em Code/Analysis existe o notebook [DataAnalysisExploration](../Code/Analysis/Data%20Analysis%20-%20Exploratory%20Data%20Analysis.ipynb). Neste notebook encontra-se a análise exploratória de dados responsável pelo melhor entendimento das informações do projeto.

## 5 - Modelagem

Em Code/Model existe o notebook [DataModeling](../Code/Model/Model%20-%20Clusterization.ipynb). Neste notebook são aplicadas técnicas de normalização de dados, clusterização e validações de qualidade de dados. 
