from rest_framework import serializers
from core.models import Donador
class DonadorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donador
        fields = ['id','Nombre','Correo','Numero']