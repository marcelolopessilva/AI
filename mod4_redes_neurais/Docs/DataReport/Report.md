
# Relatório de Dados

Esse relatório das bases de dados do projeto. A estrutura do arquivo mostra que os documentos foram fragmentados por nível de hierarquia do documento.xxxxxxxxxx


## Bases de dados

|Nome Dataset|Origem|Destino|Script|
| :---:| ---: | ---: | ---: |
mpo_fragmentos.xlsx|ONS|Pasta Data/Raw|[DataAnalysisExplorations.ipynb](../../Code/Analysis/DataAnalysisExploration.ipynb)|

</br>

**mpo_fragmentos.xlsx** - Apresenta o seguinte formato

| Nome Coluna | Descrição |
| ---:| ---: |
id| Identificador numérico no sistema de origem da empresa
Level | Nível na numeração da documentação Ex.: 1, 2, 2.1, 2.1.3
MpoEquipamentos | Nome do Equipamento
StatusDocumento| Indica se o documento está Vigente em Minuta ou Programado para Vigência
MpoIdentificador| Identificador do Documento
Tipo de Conteúdo| Informa se é um fragmento de documento ou documento inteiro
MpoEquipamentos:mrid| Identificador tipo guid gerado pelo sistema
MpoAreaEletrica| Agrupamento lógico de equipamentos por Área elétrica 
MpoCentro| Centro de Operação responsável pela execução da manobra
MpoLigadoDesligado| Indica se é uma IO de energização (ligado) ou desenergizaçao (desligado)
Hierarquia| nível hierárquico no documento
Identificador exclusivo| Identificador exclusivo do documento/fragmento
MpoEquipamentos:agenteoperador| Agente Operador do equipamento
MpoEquipamentos:agenteproprietario| Agente Proprietário do equipamento
MpoEquipamentos:centro| Centro de Operação ao qual o equipamento está realacionado
MpoEquipamentos:chave| Chave do equipamento. Identificador
MpoEquipamentos:codagenteoperador| Código do Agente Operador do equipamento
MpoEquipamentos:codagenteproprietario| Código do Agente Proprietário do equipamento
MpoEquipamentos:codigoareaeletrica| Código da área elétrica do equipamento
MpoEquipamentos:codigoons| Código do equipamento no ONS
MpoEquipamentos:familia| Família do equipamento. Ex.: Transformador, Reator, Unidade Geradora, Linha de Transmissão.
MpoEquipamentos:nomegerlim| Nome do equipamento no sistema gerenciador de limites de tensão e corrente.
MpoEquipamentos:tipo| Tipo do Equipamento
MpoLocalizacaoTaxonomia| Localização do fragmento na taxonomia
MpoSubmodulo| Submódulo de Procedimento de Rede ao qual o equipamento está associado
MpoTema| Preparação para Manobras
MpoTipoDocumento| Tipo da Preparação de Manobra
Nome do Documento| Nome do Documento
Texto| Texto do fragmento
Título| Título do fragmento
Tipo de Item| Item
Caminho| Caminho relativo do fragmento no sistema de ECM (Electronic Content Management)