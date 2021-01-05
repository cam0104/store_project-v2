from django.shortcuts import render, HttpResponse
from .forms import nuevo_producto_form

def login(request):
    return render(request,"store_project_app/login.html")

def ventas(request):
    return HttpResponse("ventas")

def estadisticas(request):
    return render(request,"store_project_app/estadisticas.html")

def inventario(request):
    return HttpResponse("inventario")

def productos(request):
    form = nuevo_producto_form()
    return render(request, "store_project_app/productos.html", {'form':form})






