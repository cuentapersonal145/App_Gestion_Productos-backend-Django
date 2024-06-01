from rest_framework import serializers

from .models import *

#--------------------------------------- Serializadores por defecto ----------------------------------------#

class ArticuloSerializador(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
        
#-----------------------------------------------------------------------------------------------------------#
