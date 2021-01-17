from store_project_app.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import *
from .models import Categoria
from .models import Producto


class EstadisticasView(TemplateView):
    template_name = 'estadisticas.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['panel'] = 'Panel de Administrador'
        return context

class CategoriaListView(LoginRequiredMixin,IsSuperuserMixin,ListView):

    model = Categoria
    template_name = 'categorias.html'

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Categoria.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categoria'
        return context

class CategoriaCreateView(CreateView):
    
    model = Categoria
    form_class = nueva_categoria_form
    template_name = 'categoria_form.html'
    success_url = reverse_lazy("{% url 'AgregarCategoria' %}")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Categoria'
        context['action'] = 'add'
        return context

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = nueva_categoria_form
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('Categoria')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoría'
        context['action'] = 'edit'
        return context

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'eliminar_categoria.html'
    success_url = reverse_lazy('Categoria')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         self.object.delete()
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Categoria'
        context['action'] = 'delete'
        return context

class ProductosListView(ListView):

    model = Producto
    template_name = 'producto/productos.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Producto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        return context

class ProductoCreateView(CreateView):
    
    model = Producto
    form_class = nuevo_producto_form
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy("{% url 'AgregarProducto' %}")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un producto'
        context['action'] = 'add'
        return context

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = nuevo_producto_form
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('Productos')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Producto'
        context['action'] = 'edit'
        return context





class VentaCreateView(LoginRequiredMixin,ValidatePermissionRequiredMixin, CreateView):
    model = Venta
    form_class = nueva_venta_form
    template_name = 'venta/venta_form.html'
    success_url = reverse_lazy('Index')
    permission_required = 'store_project_app.change_categoria'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                productos = Producto.objects.filter(nombre__icontains=request.POST['term'])[0:10]
                for i in productos:
                    data = []
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e) 
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Venta'
        context['entity'] = 'Venta'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context















