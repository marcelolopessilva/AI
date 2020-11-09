from django.shortcuts import render
from rest_framework import viewsets
from .models import InsumoDou, RelatorioDou
from .serializers import InsumoDouSerializer, RelatorioDouSerializer
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# ViewSets define the view behavior.
class InsumoDouViewSet(viewsets.ModelViewSet):

    #Ativa filtro de backend, busca genêrica e ordenação para as informações abaixo. obs: por filtro direto busca exata, por search busca tipo 'like'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = search_fields = ['nome','secao','categoria','cod_interesse','dsc_texto','dsc_objeto']
    ordering_fields = ['dat_publicacao', 'cod_interesse', 'categoria','id']
    # Ordenação default
    ordering = ['-dat_publicacao','id']

    serializer_class = InsumoDouSerializer

    # Intercepta a consulta (GET)
    def get_queryset(self):
                 
        param_dat_inicio = self.request.query_params.get('dat_inicio', None)
        param_dat_fim = self.request.query_params.get('dat_fim', None)
        
        if param_dat_inicio is not None and param_dat_fim is not None:
            # Converte parâmetros de entrada em datas. Aguarda dd/mm/aaaa
            dat_inicio = datetime.strptime(param_dat_inicio, '%d/%m/%Y')
            dat_fim = datetime.strptime(param_dat_fim, '%d/%m/%Y')

            #Filtrar o dia ou intervalo
            if dat_inicio == dat_fim:
                result = InsumoDou.objects.filter(dat_publicacao=dat_inicio)
            else:
                result = InsumoDou.objects.filter(dat_publicacao__gte=dat_inicio,dat_publicacao__lte=dat_fim)   
        else:
            # Retorna todos os resultados caso não sejam passados parâmetros
            result = InsumoDou.objects.all()
        return result

    #Intercepta a criação (PATCH)
    def partial_update(self, request, *args, **kargs):
        try:
            insumodou = self.get_object()
            
            if request.data.get('dsc_texto'):
                InsumoDou.update_classification(insumodou, request.data.get('dsc_texto'))
            else:
                raise("Informação de texto do DOU é obrigatória.")

            # Monta resposta com identificador e código de interesse previsto pelo modelo
            response = {
                        "id": insumodou.id,
                        "cod_interesse": InsumoDou.COD_INTERESSE_DICT.get(insumodou.cod_interesse),
                        "msg":"Classificação realizada"
                       }
            response_status = status.HTTP_200_OK    
        except Exception as e:
            # Monta resposta com erro
            response = {
                        "id": 0,
                        "cod_interesse": "",
                        "msg": str(e)
                       }
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR    
        finally:
            return Response(response, response_status)    
class RelatorioDouViewSet(viewsets.ModelViewSet):

    serializer_class = RelatorioDouSerializer

    queryset = RelatorioDou.objects.all()

class Dashboard(APIView):
       
    def get(self, request):
       return render(request, 'dashboard.html')