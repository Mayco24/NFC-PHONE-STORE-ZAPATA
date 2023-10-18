from django import forms
from django.core.validators import MinValueValidator

class DevicesFormulariosBase(forms.Form):
    titulo = forms.CharField(max_length=30)
    marca =  forms.CharField(max_length=10)
    modelo = forms.CharField(max_length=15)
    estado = forms.CharField(max_length=10)
    precio = forms.DecimalField(
        validators=[MinValueValidator(1)],
        widget=forms.NumberInput(attrs={'min': 1}),
        required=True
    )

class Crear_EquiposFormulario(DevicesFormulariosBase):
    ...

class Editar_EquiposFormulario(DevicesFormulariosBase):
    ...
    
class EquiposBusquedaFormularios(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)


    