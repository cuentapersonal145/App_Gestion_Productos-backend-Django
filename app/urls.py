from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('articulo', ArticuloViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
]