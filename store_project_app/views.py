from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
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

       

# class CategoriaForm(FormView):
#     form_class = nueva_categoria_form
#     template_name = 'store_project_app/categoria_form.html'
#     success_url = reverse_lazy('Categoria')

#     def form_valid(self, form):

#         return super().form_invalid(form)


#     def form_invalid(self, form):

#         print(form.errors)
#         return super().form_invalid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Form Categoria'
#         context['action'] = 'add'
#         return context

















