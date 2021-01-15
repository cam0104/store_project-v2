from django import forms
from django.forms import ModelForm
from .models import *

class nuevo_producto_form(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save() 
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class nueva_categoria_form(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        exclude = ['creacion_user','actualizacion_usuario']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save() 
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



 
    

