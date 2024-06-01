from rest_framework import viewsets

from .models import *
from .serializers import *

#--------------------------------------- API´s por defecto ----------------------------------------#

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializador

#--------------------------------------------------------------------------------------------------#