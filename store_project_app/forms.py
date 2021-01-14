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


class nueva_venta_form(ModelForm):

    class Meta:
        model = Venta
        fields = ('id_cliente','id_empleado','fecha_venta','forma_pago','precio_total')
        labels = {
            'id_cliente' : 'Cliente',
            'id_empleado' : 'Empleado',
            'fecha_venta' : 'Fecha',
            'forma_pago' : 'Forma de pago',
            'precio_total' : 'Precio total'
        }

    def __init__(self, *args, **kwargs):
        super(nueva_venta_form,self).__init__(*args,*kwargs)
 
    

