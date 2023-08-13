"""
URL configuration for ApiPeC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Precos.views import Precos_Viewset
from caixas.views import *


router = routers.DefaultRouter()
router.register('precos',Precos_Viewset,basename='Precos')
router.register('hf/caixas', Caixas_Hf_Viewset, basename='Caixas Hf')
router.register('sm/caixas', Caixas_Sm_Viewset,basename='Caixas SM')
router.register("hf/entradaNotas", Entrada_de_notas_Hf_Viewset, basename="Notas HF")
router.register("sm/entradaNotas", Entrada_de_notas_Sm_Viewset, basename="Notas Sm")
router.register('hf/sangria', Sangria_Hf_Viewset, basename='Sangria Hf')
router.register('sm/sangria', Sangria_Sm_Viewset, basename='Sangria Sm')




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
