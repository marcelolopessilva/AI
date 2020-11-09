# mit_data_science

Trabalho do bloco 2 de classificadores supervisionados

Como usar:

Todo o código foi desenvolvido em python em ambiente linux - Ubuntu vr. 20

## 1 - Instale o pacote gerenciador de dependências

Todas as dependências foram instaladas utilizando a ferramenta [pipenv](https://pypi.org/project/pipenv/) vr. version 11.9.0

* Siga as instruções do link acima para instalar o pipenv
* Para instalar as dependências deste projeto use:$ pipenv install --dev

### Dependências necessárias

django-dash==0.5.6
  - django-autoslug-iplweb [required: Any, installed: 1.9.5]
  - django-nine [required: >=0.1.1, installed: 0.2.3]
  - django-tinymce [required: >=2.0.0, installed: 3.0.2]
  - easy-thumbnails [required: >=2.4.1, installed: 2.7]
    - django [required: <4.0,>=1.11, installed: 3.1.1]
      - asgiref [required: ~=3.2.10, installed: 3.2.10]
      - pytz [required: Any, installed: 2020.1]
      - sqlparse [required: >=0.2.2, installed: 0.3.1]
    - pillow [required: Any, installed: 7.2.0]
  - feedparser [required: >=5.1.3, installed: 5.2.1]
  - ordereddict [required: >=1.1, installed: 1.1]
  - pif [required: >=0.5,<1.0, installed: 0.8.2]
    - argparse [required: Any, installed: 1.1]
    - requests [required: >=1.2.3, installed: 2.24.0]
      - certifi [required: >=2017.4.17, installed: 2020.6.20]
      - chardet [required: <4,>=3.0.2, installed: 3.0.4]
      - idna [required: <3,>=2.5, installed: 2.10]
      - urllib3 [required: <1.26,!=1.25.0,!=1.25.1,>=1.21.1, installed: 1.25.10]
  - Pillow [required: >=2.1.0, installed: 7.2.0]
  - six [required: >=1.9, installed: 1.15.0]
  - transliterate [required: >=1.5,<2.0, installed: 1.10.2]
    - six [required: >=1.1.0, installed: 1.15.0]
  - Unidecode [required: Any, installed: 1.1.1]
  - vishap [required: >=0.1.3,<2.0, installed: 0.1.5]
    - six [required: >=1.4.1, installed: 1.15.0]
django-filter==2.3.0
  - Django [required: >=2.2, installed: 3.1.1]
    - asgiref [required: ~=3.2.10, installed: 3.2.10]
    - pytz [required: Any, installed: 2020.1]
    - sqlparse [required: >=0.2.2, installed: 0.3.1]
django-plotly-dash==1.4.2
  - dash [required: >=1.11, installed: 1.16.0]
    - dash-core-components [required: ==1.12.0, installed: 1.12.0]
    - dash-html-components [required: ==1.1.1, installed: 1.1.1]
    - dash-renderer [required: ==1.8.0, installed: 1.8.0]
    - dash-table [required: ==4.10.1, installed: 4.10.1]
    - Flask [required: >=1.0.2, installed: 1.1.2]
      - click [required: >=5.1, installed: 7.1.2]
      - itsdangerous [required: >=0.24, installed: 1.1.0]
      - Jinja2 [required: >=2.10.1, installed: 2.11.2]
        - MarkupSafe [required: >=0.23, installed: 1.1.1]
      - Werkzeug [required: >=0.15, installed: 1.0.1]
    - flask-compress [required: Any, installed: 1.5.0]
      - brotli [required: Any, installed: 1.0.9]
      - flask [required: Any, installed: 1.1.2]
        - click [required: >=5.1, installed: 7.1.2]
        - itsdangerous [required: >=0.24, installed: 1.1.0]
        - Jinja2 [required: >=2.10.1, installed: 2.11.2]
          - MarkupSafe [required: >=0.23, installed: 1.1.1]
        - Werkzeug [required: >=0.15, installed: 1.0.1]
    - future [required: Any, installed: 0.18.2]
    - plotly [required: Any, installed: 4.9.0]
      - retrying [required: >=1.3.3, installed: 1.3.3]
        - six [required: >=1.7.0, installed: 1.15.0]
      - six [required: Any, installed: 1.15.0]
  - dash-core-components [required: Any, installed: 1.12.0]
  - dash-html-components [required: Any, installed: 1.1.1]
  - dash-renderer [required: Any, installed: 1.8.0]
  - Django [required: >=2.2, installed: 3.1.1]
    - asgiref [required: ~=3.2.10, installed: 3.2.10]
    - pytz [required: Any, installed: 2020.1]
    - sqlparse [required: >=0.2.2, installed: 0.3.1]
  - dpd-components [required: Any, installed: 0.1.0]
  - Flask [required: >=1.0.2, installed: 1.1.2]
    - click [required: >=5.1, installed: 7.1.2]
    - itsdangerous [required: >=0.24, installed: 1.1.0]
    - Jinja2 [required: >=2.10.1, installed: 2.11.2]
      - MarkupSafe [required: >=0.23, installed: 1.1.1]
    - Werkzeug [required: >=0.15, installed: 1.0.1]
  - plotly [required: Any, installed: 4.9.0]
    - retrying [required: >=1.3.3, installed: 1.3.3]
      - six [required: >=1.7.0, installed: 1.15.0]
    - six [required: Any, installed: 1.15.0]
djangorestframework==3.11.1
  - django [required: >=1.11, installed: 3.1.1]
    - asgiref [required: ~=3.2.10, installed: 3.2.10]
    - pytz [required: Any, installed: 2020.1]
    - sqlparse [required: >=0.2.2, installed: 0.3.1]
ipykernel==5.3.4
  - ipython [required: >=5.0.0, installed: 7.18.1]
    - backcall [required: Any, installed: 0.2.0]
    - decorator [required: Any, installed: 4.4.2]
    - jedi [required: >=0.10, installed: 0.17.2]
      - parso [required: >=0.7.0,<0.8.0, installed: 0.7.1]
    - pexpect [required: >4.3, installed: 4.8.0]
      - ptyprocess [required: >=0.5, installed: 0.6.0]
    - pickleshare [required: Any, installed: 0.7.5]
    - prompt-toolkit [required: >=2.0.0,!=3.0.0,<3.1.0,!=3.0.1, installed: 3.0.7]
      - wcwidth [required: Any, installed: 0.2.5]
    - pygments [required: Any, installed: 2.6.1]
    - setuptools [required: >=18.5, installed: 46.1.3]
    - traitlets [required: >=4.2, installed: 5.0.4]
      - ipython-genutils [required: Any, installed: 0.2.0]
  - jupyter-client [required: Any, installed: 6.1.7]
    - jupyter-core [required: >=4.6.0, installed: 4.6.3]
      - traitlets [required: Any, installed: 5.0.4]
        - ipython-genutils [required: Any, installed: 0.2.0]
    - python-dateutil [required: >=2.1, installed: 2.8.1]
      - six [required: >=1.5, installed: 1.15.0]
    - pyzmq [required: >=13, installed: 19.0.2]
    - tornado [required: >=4.1, installed: 6.0.4]
    - traitlets [required: Any, installed: 5.0.4]
      - ipython-genutils [required: Any, installed: 0.2.0]
  - tornado [required: >=4.2, installed: 6.0.4]
  - traitlets [required: >=4.1.0, installed: 5.0.4]
    - ipython-genutils [required: Any, installed: 0.2.0]
Markdown==3.2.2
pandas==1.1.2
  - numpy [required: >=1.15.4, installed: 1.19.1]
  - python-dateutil [required: >=2.7.3, installed: 2.8.1]
    - six [required: >=1.5, installed: 1.15.0]
  - pytz [required: >=2017.2, installed: 2020.1]
sklearn==0.0
  - scikit-learn [required: Any, installed: 0.23.2]
    - joblib [required: >=0.11, installed: 0.16.0]
    - numpy [required: >=1.13.3, installed: 1.19.1]
    - scipy [required: >=0.19.1, installed: 1.5.2]
      - numpy [required: >=1.14.5, installed: 1.19.1]
    - threadpoolctl [required: >=2.0.0, installed: 2.1.0]

## 2 - Execute a WEB API do DOU

* Em Code/Operationalization digite no terminal: python manage.py runserver

    * As 3 últimas linhas devem ser:
        * Django version 3.1.1, using settings 'services.settings'
        * Starting development server at http://127.0.0.1:8000/
        * Quit the server with CONTROL-C.

* Acesse o endereço no browser: http://127.0.0.1:8000/api/v1/
    * A tela com a informação dos serviços da API deve ser disponibilizada
* Acesse o endereço no browser: http://127.0.0.1:8000/dash para ter acesso ao dashboard operacional

## 3 Operação Diária

* Em Code/Operationalization/applications existe o notebook [0-PipelineOperacaoDiaria](./Code/Operationalization/applications/0-PipelineOperacaoDiaria.ipynb). Este notebook é responsável pela execução dos outros 3 notebook que executam o processo operacional diário.
    * [1-AquisicaoDadosAPI](./Code/Operationalization/applications/1-AquisicaoDadosAPI.ipynb) - Baixa os arquivos zip do dia do site da imprensa nacional com as informações do DOU utilizando RPA (Robotic Process Automation)
    * [2-PreparacaoDadosAPI](./Code/Operationalization/applications/2-PreparacaoDadosAPI.ipynb) - Extrai arquivos xml dos arquivos zip, os prepara e insere na base SQLLite que é utilizada pela WEBAPI
    * [3-AquisicaoNovosDadoseScoring](./Code/Operationalization/applications/3-AquisicaoNovosDadoseScoring.ipynb) - Faz a aquisição dos dados diários e realiza seus scorings via WEB API


Uma apresentação detalhada do projeto "Arquitetura BDREG.pptx" pode ser encontrada em /Docs/Project/Arquitetura BDREG.pptx

## 4 Retreino do Modelo

* O retreino do modelo pode ser realizado utilizando o notebook [DataModeling](./Code/Model/DataModeling.ipynb)