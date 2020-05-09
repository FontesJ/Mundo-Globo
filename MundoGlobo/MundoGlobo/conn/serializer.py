from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'nome', 'email', 'sexo', 'senha', 'foto', 'data_pub')