from django.urls import path
from . import views
app_name = 'empleados_app'
urlpatterns = [
   path('empleado/lista-empleados/', views.lista_empleados, name='lista-empleados'),
   path('empleado/crear-empleados/', views.CrearEmpleado.as_view(), name='crear-empleados'),
]