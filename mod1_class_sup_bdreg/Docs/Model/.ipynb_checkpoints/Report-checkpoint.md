# Relatório de Modelagem

Documento para registrar as análises e a modelagem desenvolvida.


## Análise de Dados

Os dados com os comentários das avaliações foram processados para a criação de novas features.
O processamento consiste em contar a quantidade de vezes que cada palavra é escrita nos comentários. Essa contagem é feita por avaliação.

Alguns processos de normalização foram utilizados, como o Tf-Idf (Term Frequency, Inverse Document Frequency). A contagem de cada palavra é normalizada pela quantidade de documentos que essa palavra aparece. Palavras que aparecem em todos as avaliações teriam um Idf alto, logo diminuindo o valor da feature para essa palavra.

### Contagem de palavras

Foram observadas palavras com contagens superiores a 8.000. Pode-se ver que a distribuição da contagem de palavras segue uma distribuição exponecial.

A palavra mais comum é *basis*. Embora seja mais comum, ela parece não ter poder de classificação, uma vez que a sua contagem por classe parece ser próxima.

Já outros termos menos frequentes, como *movie starts* parece ser mais frequente em comentários de sentimento positivo.

### Normalização por TfIdf

Os resultados da normalização mostraram que a distribuição das features de cada palavra tem uma calda menos longa que o distribuição da contagem das palavras.

O valor médio das features normalizadas por TfIdf diferen quando calculado para os comentários de cada classe. Pode-se observar que algumas palavras que não eram frequentes, como *tries* possui uma diferença considerável no seu valor médio quando calculado para as classes.

### Árvore de Decisão

De forma preliminar, foi feita a análise de uma árvore de decisão de profundidade 10. Sem o compromisso com a generalização do classificador, obteve-se um valor de f1-score igual a 86%.

Para essa classificação, podemos observar a curva de importância das features. Pode-se ver que a palavra mais importante para o classificador foi o termo *tries*, seguido de *happens* e *cinematic*.


## Próximos passos

Após a análise preliminar, devemos seguir com o treinamento dos modelos de classificação, utilizando validação cruzada como forma de estimar os hiper-parâmetros do modelo que conseguem a melhor generalização possível.

