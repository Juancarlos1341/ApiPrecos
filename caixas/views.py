from rest_framework import viewsets
from caixas.models import *
from caixas.serializer import *

class Caixas_Hf_Viewset(viewsets.ModelViewSet):
    queryset = CaixasHf.objects.all()
    serializer_class = Caixas_Hf_Serializer
    search_fields = ['=Codigo', 'DataInicial']


class Caixas_Sm_Viewset(viewsets.ModelViewSet):
    queryset = CaixasSm.objects.all()
    serializer_class = Caixas_Sm_Serializer
    search_fields = ['=Codigo','DataInicial']

class Entrada_de_notas_Hf_Viewset(viewsets.ModelViewSet):
    queryset = Entrada_de_notas_Hf.objects.all()
    serializer_class = Entrada_de_notas_Hf_Serializer
    search_fields = ['=Codigo','Fornecedor']

class Entrada_de_notas_Sm_Viewset(viewsets.ModelViewSet):
    queryset = Entrada_de_notas_Sm.objects.all()
    serializer_class = Entrada_de_notas_Sm_Serializer
    search_fields = ['=Codigo','Fornecedor']

class Sangria_Hf_Viewset(viewsets.ModelViewSet):
    queryset = Sangria_Hf.objects.all()
    serializer_class = Sangria_Hf_Serializer
    search_fields = ['=Codigo','Descriacao']

class Sangria_Sm_Viewset(viewsets.ModelViewSet):
    queryset = Sangria_Sm.objects.all()
    serializer_class = Sangria_Sm_Serializer
    search_fields = ['=Codigo','=Data']
    
