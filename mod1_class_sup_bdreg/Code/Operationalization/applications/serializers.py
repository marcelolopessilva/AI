from rest_framework import serializers
from .models import InsumoDou, RelatorioDou
from datetime import date
from django.utils import timezone

# Serializers define the API representation.

# Serializa os dados di banco de dados em json que será retornado pela API
class InsumoDouSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = InsumoDou
        fields = ['id','nome','secao','dat_publicacao','categoria','num_pagina','url_pdf','id_materia','dsc_texto','din_validacao','cod_interesse', 'num_edicao', 'dsc_objeto', 'dsc_ementa']

class RelatorioDouSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = RelatorioDou
        fields = ['num_dia','dsc_interesse','num_quantidade']