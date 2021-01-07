from django.urls import path
from store_project_app import views

urlpatterns = [
    path('', views.login, name = "Login"),
    path('ventas', views.ventas, name = 'Ventas'),
    path('estadisticas', views.estadisticas, name = "Estadisticas"),
    path('inventario', views.inventario, name = 'Inventario'),
    path('productos', views.productos, name = 'Productos'),
    path('delete/<int:id>/', views.delete_productos, name = 'DeleteProducto'),
    path('<int:id>/', views.modificar_producto, name = 'modificarProductoc'),
    


]