from django import forms
from django.forms import ModelForm, widgets
from .models import *


class nuevo_producto_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fecha_vencimiento'].widget.attrs = {
            'autocomplete': 'off',
            'class': 'form-control datetimepicker-input',
            'id': 'fecha_vencimiento',
            'data-target': '#fecha_vencimiento',
            'data-toggle': 'datetimepicker'

        }

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
        exclude = ['creacion_user', 'actualizacion_usuario']

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_empleado'].widget.attrs = {
            'type' : 'field',

        }

        self.fields['fecha_venta'].widget.attrs = {
            'readonly': True
        }

        self.fields['precio_total'].widget.attrs = {
            'readonly': True
        }

    class Meta:
        model = Venta
        fields = '__all__'
        exclude = ['creacion_user', 'actualizacion_usuario']

        #     'fecha_venta': widgets.DateInput(format='%Y-%m-%d', attrs={'value': datetime.now().strftime('%Y-%m-%d'), }),

        # }
