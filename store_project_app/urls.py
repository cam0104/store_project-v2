from django.urls import path
from store_project_app import views

urlpatterns = [
    path('index', views.index, name = 'Index'),
    path('estadisticas', views.estadisticas, name = 'Estadisticas'),
    # path('', views.login, name = "Login"),
    # path('ventas', views.nueva_venta, name = 'Ventas'),
    # path('estadisticas', views.estadisticas, name = "Estadisticas"),
    # path('inventario', views.inventario, name = 'Inventario'),
    path('categoria', views.CategoriaListView.as_view(), name = 'Categoria'),
    path('agregar_categoria', views.CategoriaCreateView.as_view(), name = 'AgregarCategoria'),
    path('editar_categoria/<int:pk>/', views.CategoriaUpdateView.as_view(), name = 'EditarCategoria'),
    path('eliminar_categoria/<int:pk>/', views.CategoriaDeleteView.as_view(), name = 'EliminarCategoria'),


    path('productos', views.ProductosListView.as_view(), name = 'Productos'),
    path('delete/<int:id>/', views.delete_productos, name = 'DeleteProducto'),
    path('<int:id>/', views.modificar_producto, name = 'modificarProducto'),

    
    
    


]