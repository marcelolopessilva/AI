from django.db import models
from services import globalTrainResults
from datetime import datetime

# Modelo com as informações de insumo do DOU
class InsumoDou(models.Model):
    
    COD_INTERESSE = (
        ('SI', 'Sem Interesse'),
        ('DI', 'De Interesse'),
        ('NA', 'Não avaliado'),
    )

    COD_INTERESSE_DICT = dict((x, y) for x, y in COD_INTERESSE)

    id = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=100)
    secao = models.CharField(max_length=10)
    dat_publicacao = models.DateTimeField()
    categoria = models.CharField(max_length=500)
    num_pagina = models.CharField(max_length=10)
    url_pdf = models.URLField()
    id_materia = models.CharField(max_length=50)
    dsc_texto = models.TextField()
    din_validacao = models.DateTimeField(null=True)
    cod_interesse = models.CharField(max_length=2, choices=COD_INTERESSE, default='NA')
    num_edicao = models.CharField(max_length=10, null =True)
    dsc_objeto = models.CharField(max_length=200, null=True)
    dsc_ementa = models.CharField(max_length=300, null=True)

    def update_classification(self, dsc_texto):

        # Carrega modelo treinado
        modelAquisicao = globalTrainResults['LogisticRegression']
        
        # Faz a predição do texto e converte para o domínio correspondente
        self.cod_interesse = 'DI' if modelAquisicao.predict([dsc_texto]) else 'SI' 
        self.din_validacao = datetime.now()
       
        self.save()

    def __str__(self):
        return self.id
		
class RelatorioDou(models.Model):
    
    num_dia = models.CharField(max_length=5, primary_key=True)
    cod_interesse = models.CharField(max_length=20)
    num_quantidade = models.IntegerField()

    #Retorna a descrição do código de interesse para montar o relatório
    @property
    def dsc_interesse(self):
        descricao = dict(InsumoDou().COD_INTERESSE)

        return descricao[self.cod_interesse]

    class Meta:
       managed = False
       db_table = 'applications_relatoriodou'

    def __str__(self):
        return self.num_dia