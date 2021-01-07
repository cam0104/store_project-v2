from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import nuevo_producto_form
from .models import *
#from .forms import nueva_categoria_form

def login(request):
    return render(request,"store_project_app/login.html")

def ventas(request):
    return HttpResponse("ventas")

def estadisticas(request):
    return render(request,"store_project_app/estadisticas.html")

def inventario(request):
    return HttpResponse("inventario")

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

def modificar_producto(request):
    return render(request, "store_project_app/productos.html", {'id':id})



# def categoria(request):
#     if request.method == 'POST':
#         fm = nueva_categoria_form(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('/productos')
#             #fm = nuevo_producto_form()

#     else:
#         fm = nueva_categoria_form()
#         #productos = Producto.objects.all()
#     return render(request, "store_project_app/productos.html", {'form_categoria':fm})











