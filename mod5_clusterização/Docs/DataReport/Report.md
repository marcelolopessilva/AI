
# Relatório de Dados

Apresenta as bases de dados do projeto. 

## Bases de dados

|Nome Dataset|Origem|Destino|Script|
| :---:| ---: | ---: | ---: |
household_power_consumption.txt|[kaggle link](https://www.kaggle.com/uciml/electric-power-consumption-data-set)|Pasta Data/Raw|[Data Preparation](../../Code/DataPrep/Data%20Preparation%20-%20Household%20comsumption.ipynb)|

</br>

household_power_consumption.txt - Apresenta o seguinte formato

| Nome Coluna | Descrição |
| ---:| ---: |
date| Data no formato dd/mm/yyyy
time| Hora no formato hh:mm:ss
globalactivepower| Potência ativa global medida por minuto (em kilowatt - kW)
globalreactivepower| Potência reativa global medida por minuto (em voltampere reativo - VAr)
voltage| Voltagem medida por minuto (em volt - V)
global_intensity| Corrente medida por minuto (em ampere - A)
submetering1| Energia medida por hora da subárea 1. Corresponde a cozinha que contém monitorados os seguintes aparelhos: lava louças, um microondas e um forno elétrico. (em Watt Hora - Wh)
submetering2| Energia medida por hora da subárea 2. Corresponde a lavanderia que contém monitorados os seguintes aparelhos: lava roupas, secadora, um refrigerador e um ponto de luz. (em Watt Hora - Wh)
submetering3| Energia medida por hora da subárea 3. Contém monitorados os seguintes aparelhos: aquecedor de água e um ar condicionado. (em Watt Hora - Wh)