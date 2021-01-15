

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from store_project_app.forms import nueva_venta_form
from store_project_app.models import Venta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin


# class VentaCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
#     model = Venta
#     form_class = nueva_venta_form
#     template_name = 'venta/venta_form.html'
#     success_url = reverse_lazy('Index')
#     url_redirect = success_url

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e) 
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Crear una Venta'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context
