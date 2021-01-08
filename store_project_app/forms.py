from django import forms
from django.forms import ModelForm
from .models import Producto, Categoria

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
    

