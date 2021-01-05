from django import forms
from .models import Producto

class nuevo_producto_form(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ('__all__')

