from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.generic import ListView
from .forms import *
from .models import Categoria
from .models import Producto
#from .forms import nueva_categoria_form

# def login(request):
#     return render(request,"store_project_app/login.html")

# def nueva_venta(request):
#     if request.method == 'POST':
#         fm = nueva_venta_form(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('/nueva_venta')
#             #fm = nuevo_producto_form()

#     else:
#         fm = nueva_venta_form()
#     productos = Producto.objects.all()
#     return render(request, "store_project_app/nueva_venta.html", {'form_venta':fm, 'productos':productos})


def estadisticas(request):
    return render(request,"store_project_app/estadisticas.html")

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
    template_name = 'store_project_app/categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categorias'
        return context


    # if request.method == 'POST':
    #     fm = nueva_categoria_form(request.POST)
    #     if fm.is_valid():
    #         fm.save()
    #         return redirect('/categoria')
    # else:
    #     fm = nueva_categoria_form()
    # return render(request, "store_project_app/categoria.html", {'form_categoria':fm})

# def listarCategoria(request):
#     data = {
#         'title' : 'Listado de categorias',
#         'categorias' : Categoria.objects.all()
        
#     }
#     return render(request, "store_project_app/categoria.html", data)














