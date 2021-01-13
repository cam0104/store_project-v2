from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from .forms import *
from .models import Categoria
from .models import Producto

def estadisticas(request):

    data = {
        'title' : 'Estadisticas'
    }
    return render(request,"store_project_app/estadisticas.html", data)

def index(request):
    return render(request,"store_project_app/index.html")

def productos(request):
    if request.method == 'POST':
        fm = nuevo_producto_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/productos')
            #fm = nuevo_producto_form()

    else:
        fm = nuevo_producto_form()
    productos = Producto.objects.all()
    return render(request, "store_project_app/productos.html", {'form_producto':fm, 'productos':productos})

def delete_productos(request, id):
    if request.method == 'POST':
        producto = Producto.objects.get(pk=id)
        producto.delete()
        return HttpResponseRedirect('/productos')

def modificar_producto(request, id):
    if request.method == 'POST':
        pi = Producto.objects.get(pk=id)
        fm = nuevo_producto_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Producto.objects.get(pk=id)
        fm = nuevo_producto_form(instance=pi)
    return render(request, "store_project_app/productos.html", {'form':fm})


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'store_project_app/categorias.html'

    @csrf_exempt
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
    template_name = 'store_project_app/categoria_form.html'
    success_url = reverse_lazy("{% url 'AgregarCategoria' %}")

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
    template_name = 'store_project_app/categoria_form.html'
    success_url = reverse_lazy('Categoria')

    # def dispatch(self, request, *args, **kwargs):
    #     object = self.get_object()
    #     return super().dispatch(self, request, *args, **kwargs)

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
    template_name = 'store_project_app/categorias.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Categoria'
        context['action'] = 'delete'
        return context


class ProductosListView(ListView):
    model = Producto
    template_name = 'store_project_app/productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Producto'
        return context


















