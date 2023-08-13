from rest_framework import serializers
from caixas.models import *

class Caixas_Hf_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CaixasHf
        exclude = []

class Caixas_Sm_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CaixasSm
        exclude = []

class Entrada_de_notas_Hf_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada_de_notas_Hf
        exclude = []

class Entrada_de_notas_Sm_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada_de_notas_Sm
        exclude = []

class Sangria_Hf_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sangria_Hf
        exclude = []

class Sangria_Sm_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sangria_Sm
        exclude = []