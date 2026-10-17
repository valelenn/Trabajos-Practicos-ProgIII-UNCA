from django.urls import path #Funcion para crear regla de rutas
from . import views  # el punto '.' significa "esta misma carpeta"

app_name = 'reservas'

urlpatterns = [
    path('', views.lista_actividades, name='lista_actividades'),
    path('agregar/', views.agregar_actividad, name='agregar_actividad'),
    path('<int:pk>/', views.detalle_actividad, name='detalle_actividad'),
]