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
    if request.method == 'POST':
        fm = nuevo_producto_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = nuevo_producto_form()

    else:
        fm = nuevo_producto_form()
    return render(request, "store_project_app/productos.html", {'form_producto':fm})






