from django import forms #Para construir formularios
from .models import ActividadDeportiva #Traemos el modelo del tp6

class ActividadDeportivaForm(forms.ModelForm): #Formulario vinculado a una tabla de BD
    class Meta:
        model = ActividadDeportiva # Revisa la tabla de Actividad deportiva como molde
        fields = ['nombre', 'descripcion', 'lugar', 'cupo'] #Campos que aparecen en pantalla
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la actividad'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada...'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Polideportivo'}),
            'cupo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad máxima de participantes'}),
        }