from django.shortcuts import render
from .models import Empleado
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def lista_empleados(request):
    datos = {
        'lista': Empleado.objects.all().order_by('nombre'),
        'titulo': 'Lista de empleados',
    }
    return render(request, 'empleados/lista-empleados.html',datos)

class CrearEmpleado(CreateView):
    template_name = 'empleados/crear-empleado.html'
    model = Empleado
    fields = [ 'nombre', 'correo', 'sueldo' ]
    success_url = reverse_lazy ('empleados_app:lista-empleados')