from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ActividadDeportiva
from .forms import ActividadDeportivaForm

# 1. Vista para listar todas las actividades
def lista_actividades(request):
    actividades = ActividadDeportiva.objects.all()
    return render(request, 'reservas/lista_actividades.html', {'actividades': actividades})

# 2. Vista para ver el detalle de una actividad (o 404 si no existe)
def detalle_actividad(request, pk): #Como estoy consultando, recibe una pk
    actividad = get_object_or_404(ActividadDeportiva, pk=pk)
    return render(request, 'reservas/detalle_actividad.html', {'actividad': actividad})

# 3. Vista para registrar una nueva actividad (GET muestra form, POST procesa y guarda)
def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadDeportivaForm(request.POST)
        if form.is_valid():
            nueva_actividad = form.save()
            messages.success(request, f'La actividad "{nueva_actividad.nombre}" se registró correctamente.')
            return redirect('reservas:detalle_actividad', pk=nueva_actividad.pk)
    else:
        form = ActividadDeportivaForm()

    return render(request, 'reservas/agregar_actividad.html', {'form': form})