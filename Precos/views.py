from rest_framework import viewsets
from Precos.models import Precos
from Precos.serializer import Precos_Serializer


class Precos_Viewset(viewsets.ModelViewSet):
    queryset = Precos.objects.all()
    serializer_class = Precos_Serializer
    search_fields = ['Produto','=Codigo']
    