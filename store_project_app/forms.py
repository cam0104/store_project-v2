from django import forms
from django.forms import ModelForm
from .models import *

class nuevo_producto_form(ModelForm):

    class Meta:
        model = Producto 
        fields = ('id_producto','id_categoria','nombre','descripcion','stock','precio','fecha_vencimiento')
        labels = {
            'id_categoria' : 'Categoria'
        }

    def __init__(self, *args, **kwargs):
        super(nuevo_producto_form,self).__init__(*args,*kwargs)
        #self.fields['Categoria'].empty_label = "Seleccionar Categoria"
        #self.fields['fecha_vencimiento'].required = False

class nueva_categoria_form(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

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
 
    

