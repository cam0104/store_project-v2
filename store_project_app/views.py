import traceback
from store_project_app.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import *
import json
from .models import Categoria
from .models import Producto
from .models import Detalle_Venta



import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class EstadisticasView(TemplateView):
    template_name = 'estadisticas.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estadisticas'
        return context


class CategoriaListView(LoginRequiredMixin, IsSuperuserMixin, ListView):
    model = Categoria
    template_name = 'categorias.html'

    @method_decorator(csrf_exempt)
    # @method_decorator(login_required)
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


class VentaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
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
                productos = Producto.objects.filter(
                    nombre__icontains=request.POST['term'])[0:10]
                for i in productos:
                    data = []
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)

            elif action == 'add':
                ventas = json.loads(request.POST['ventas'])
                venta = Venta()
                venta.id_cliente = Cliente.objects.get(id_cliente = ventas['id_cliente'])
                venta.id_empleado = Empleado.objects.get(id_empleado = ventas['id_empleado'])
                venta.fecha_venta = ventas['fecha_venta']
                venta.forma_pago = Metodo_Pago.objects.get(id_metodo_pago = ventas['forma_pago'])
                venta.precio_total = float(ventas['precio_total'])
                venta.save()

                for i in ventas['productos']:
                    detalle_venta = Detalle_Venta()
                    detalle_venta.id_venta = Venta.objects.get(id_venta = venta.id_venta)
                    detalle_venta.id_producto = Producto.objects.get(id_producto = i['id_producto'])
                    detalle_venta.cantidad = int(i['cantidad'])
                    detalle_venta.subtotal = float(i['subtotal'])
                    detalle_venta.save()

                data = {'id': venta.id_venta}
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
            track = traceback.format_exc()
            print(track)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Venta'
        context['entity'] = 'Venta'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
        
class VentaListView(ListView):

    model = Venta
    template_name = 'venta/consultar_venta.html'

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
                for i in Venta.objects.all():
                    data.append(i.toJSON())
            elif action == 'searchdata_detalle':
                data = []
                for i in Detalle_Venta.objects.filter(id_venta=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        return context
        

# class VentaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
#     model = Venta
#     form_class = nueva_venta_form
#     template_name = 'venta/venta_form.html'
#     success_url = reverse_lazy('Index')
#     permission_required = 'store_project_app.change_categoria'
#     url_redirect = success_url

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'autocomplete':
#                 productos = Producto.objects.filter(
#                     nombre__icontains=request.POST['term'])[0:10]
#                 for i in productos:
#                     data = []
#                     item = i.toJSON()
#                     item['value'] = i.nombre
#                     data.append(item)

#             elif action == 'edit':
#                 ventas = json.loads(request.POST['ventas'])
#                 venta = Venta()
#                 venta.id_cliente = Cliente.objects.get(id_cliente = ventas['id_cliente'])
#                 venta.id_empleado = Empleado.objects.get(id_empleado = ventas['id_empleado'])
#                 venta.fecha_venta = ventas['fecha_venta']
#                 venta.forma_pago = Metodo_Pago.objects.get(id_metodo_pago = ventas['forma_pago'])
#                 venta.precio_total = float(ventas['precio_total'])
#                 venta.save()

#                 for i in ventas['productos']:
#                     detalle_venta = Detalle_Venta()
#                     detalle_venta.id_venta = Venta.objects.get(id_venta = venta.id_venta)
#                     detalle_venta.id_producto = Producto.objects.get(id_producto = i['id_producto'])
#                     detalle_venta.cantidad = int(i['cantidad'])
#                     detalle_venta.subtotal = float(i['subtotal'])
#                     detalle_venta.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#             track = traceback.format_exc()
#             print(track)
#         return JsonResponse(data, safe=False)

#     def get_detalle_productos(self):
#         data = []
#         try:
#             for i in Detalle_Venta.objects.filter(id_venta=self.kwargs['pk']):
#                 item = i.id_producto.toJSON()
#                 item['cantidad'] = i.cantidad
                
#                 data.append(item)
#         except Exception as e:
#             data['error'] = str(e)
#             track = traceback.format_exc()
#             print(track)

#         return data

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Edición de una Venta'
#         context['entity'] = 'Venta'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         #context['detalles'] = self.get_detalle_productos()
#         return context


class VentaFacturaPdfView(View):

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('venta/factura.html')
            context = {
                'venta': Venta.objects.get(pk=self.kwargs['pk']),
                'detalle' : Detalle_Venta.objects.filter(id_venta=self.kwargs['pk']),
                'comp': {'name':'Cacharreria El Portal', 'ruc': 'RUC', 'address': 'Direccion'}
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except Exception as e:
            track = traceback.format_exc()
            print(track)
            return HttpResponseRedirect(reverse_lazy('ListaVenta'))



     








