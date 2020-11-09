
# Relatório de Dados

Esse relatório das bases de dados do projeto.


## Bases de dados

|Nome Dataset|Origem|Destino|Script|
| :---:| ---: | ---: | ---: |
BPREG_CSVdelimited.csv|Empresa Contratante|Pasta Data/Raw||
Arquivos .zip|Site [inlabs](https://inlabs.in.gov.br/acessar.php)|Pasta Data/Raw|[1-AquisicaoDadosAPI.ipynb](./Code/Operationalization/applicatons/1-AquisicaoDadosAPI.ipynb)
Arquivos .xml|Pasta Data/Processed|Base SQLlite|[2-PreparacaoDadosAPI.ipynb](./Code/Operationalization/applicatons/2-PreparacaoDadosAPI.ipynb)
base_total|Preparação de dados após (EDA) análise exploratória de dados|Modelagem|[DataAnalysysExplorations.ipynb](./Code/Operationalization/applicatons/DataAnalysysExplorations.ipynb)
</br>

**BPREG_CSVdelimited.csv** - Apresenta o seguinte formato

| Nome Coluna | Descrição |
| ---:| ---: |
id| Identificador numérico no sistema de origem da empresa
objeto | Objeto ao qual a publicação de refere
origem | Origem no DOU composto por número e data
data_publicacao| Data da publicação do ATO ou Portaria
informacao| Texto da publicação
data_inclusao| Data de inclusão da publicação no sistema da empresa
</br>

**Arquivos .ZIP** - Arquivos no formato compactado zip, com a formatação de nome AAAA-MM-DD-DO?.zip, onde: AAAA = Ano, MM = mes, DD = dia da publicação, ? = número de 1 a 3 informando de qual seção do DOU as informações se referem. Ex.: 2020-09-03-DO1.zip

**Arquivos .XML** - Arquivos no formato xml, com a formatação de nome XXX-AAAAMMDD-YYYYYYYY.zip, onde: XXX = Numérico de 3 posições, AAAA = Ano, MM = mes, DD = dia da publicação, YYYYYYYY = Numérico com 8 posições informando o identificador do sistema de edição da imprensa nacional.

Os textos das informações são strings de 30 a 51.334 caracteres. Em média, cada informação tem comprimento de 1.443 caracteres.

Formato:
Tag XML|Tipo|Descrição
| ---:| ---: |:--- |
editionNumber|Texto|Número da edição
pdfPage|Texto|URL para acessar a página publicada em pdf
artCategory|Texto|Fornece a grade completa da matéria separado por "/"
pubDate|Data|Data de publicação da matéria em formato dd/mm/aaaa
artType|Texto|Tipo da matéria (ie. Portaria, Ato, e outros)
name|Texto|Nome da matéria no GN4, sistema editorial da Imprensa Nacional
pubName|Texto|Nome ou número da sessão (DOU1, DOU2, DOU3)
numberPage|Texto|Nº da página na qual a matéria está conectada
Identifica|Texto|Texto que identifica aquela norma na estrutura organização da origem ("Portaria 131 de 21 de março de 2017")
Texto|Texto|Conterá o conteúdo completo da matéria, do título até a assinatura/cargo obedecendo a ordem do texto. E contará com classes relacionadas a estrutura de TAGs.
</br>

Foram encontrados os seguintes valores nulos na base. Como a informação é a mais importante, só foram mantidos os registros que a contiham. No final ficaram 20.399 registros.

|Coluna|Contagem de Nulos
| ---:| ---: |     
|id|64894 
|objeto|27179 
|origem|20399 
|data_publicacao|20399 
|informacao|20399 
|data_inclusao|13619 
</br>

**base_total** - Base classificada com informações de interesse e sem interesse. Apresenta o seguinte formato:

| Nome Coluna | Descrição |
| ---:| ---: |
id| Identificador numérico no sistema de origem da empresa
objeto | Objeto ao qual a publicação de refere
origem | Origem no DOU composto por número e data
data_publicacao| Data da publicação do ATO ou Portaria
informacao| Texto da publicação
data_inclusao| Data de inclusão da publicação no sistema da empresa
interesse|Boleano com a representação 1 - Interesse, 0 - Sem Interesse
informacao_token|Texto apresentando as palavras como tokens
</br>

Analisando os textos da informação foi verificado que o mesmo continha tags e decodificações HTML. O componente [Bleach](https://bleach.readthedocs.io/en/latest/index.html) foi utilizado para realizar essa limpeza.

Ex: "\<p>O SUPERINTENDENTE DE FISCALIZA&Ccedil;&Atilde;O DOS SERVI&Ccedil;OS DE GERA\&Ccedil;&Atilde;O ..."

O próximo processo foi a diminuição de ruídos de texto, utilizando téncicas de exclusão de números entre palavras, caracteres especiais e transformação do texto em mínusculo. Os números soltos foram considerados importantes já que várias informações contam com os números de resolução de órgão importantes para o contexto do projeto como: Ministério de Minas e Energia, ANEEL, ONS, EPE, etc.

Finalmente o texto foi tokenizado utilizando a biblioteca [nltk](https://www.nltk.org/) - Natural Language Toolkit para posterior uso na Análise Exploratória de Dados. Os parâmetros foram ajustados para a geração de até 2 ngrams (bigrama).




