from django import forms
from django.forms import ModelForm, widgets
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

    # def __init(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for form in self.visible_fields():
    #         form.field.wi

    class Meta:
        model = Venta
        fields = '__all__'
        # widgets = {
        #     'id_cliente': widgets.Select(attrs={
        #         'class': 'form-control-select2',
        #         'style': 'width: 100%'
        #     }), 

        #     'fecha_venta': widgets.DateInput(format='%Y-%m-%d', attrs={'value': datetime.now().strftime('%Y-%m-%d'), }),


        # }
