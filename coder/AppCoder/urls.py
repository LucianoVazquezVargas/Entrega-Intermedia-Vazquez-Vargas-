from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio,name="inicio"),
    path("personas/",personas,name="personas"),
    path("notas/",notas,name="notas"),
    path("helado/",helado,name="helado"),
    path("busquedaHelados/",busquedaHelados,name="busquedaHelados"),
    path("buscar/",buscar,name="buscar"),

]
