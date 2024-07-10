from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.base, name='base'),
    path('aprendiz/', v.aprendiz, name='aprendiz'),
    path('agregar/', v.agregar, name='agregar'),
    path('eliminar/<int:id>/',v.eliminar, name='eliminar'),
    path('editar/<int:id>/', v.editar, name='editar'),
    path('cali/', v.cali, name='cali'),
    path('compe/', v.compe, name='compe'),
]
