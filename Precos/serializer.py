from rest_framework import serializers
from Precos.models import Precos

class Precos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Precos
        exclude = []