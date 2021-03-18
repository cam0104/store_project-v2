from django.urls import path
from store_project_app import views

urlpatterns = [
    path("estadisticas", views.EstadisticasView.as_view(), name="Estadisticas"),
    path("categoria", views.CategoriaListView.as_view(), name="Categoria"),
    path(
        "agregar_categoria",
        views.CategoriaCreateView.as_view(),
        name="AgregarCategoria",
    ),
    path(
        "editar_categoria/<int:pk>/",
        views.CategoriaUpdateView.as_view(),
        name="EditarCategoria",
    ),
    path(
        "eliminar_categoria/<int:pk>/",
        views.CategoriaDeleteView.as_view(),
        name="EliminarCategoria",
    ),
    path("productos", views.ProductosListView.as_view(), name="Productos"),
    path(
        "agregar_producto", views.ProductoCreateView.as_view(), name="AgregarProducto"
    ),
    path(
        "editar_producto/<int:pk>/",
        views.ProductoUpdateView.as_view(),
        name="EditarCategoria",
    ),
    path(
        "eliminar_producto/<int:pk>/",
        views.ProductoDeleteView.as_view(),
        name="EliminarProducto",
    ),
    path("clientes", views.ClienteListView.as_view(), name="Clientes"),
    path("agregar_cliente", views.ClienteCreateView.as_view(), name="AgregarCliente"),
    path(
        "editar_cliente/<int:pk>/",
        views.ClienteUpdateView.as_view(),
        name="EditarCliente",
    ),
    path(
        "eliminar_cliente/<int:pk>/",
        views.ClienteDeleteView.as_view(),
        name="EliminarCliente",
    ),
    path("ventas", views.VentaListView.as_view(), name="ListaVenta"),
    path("crear_venta", views.VentaCreateView.as_view(), name="Venta"),
    path(
        "factura_venta/<int:pk>/",
        views.VentaFacturaPdfView.as_view(),
        name="FacturaVenta",
    ),
    path("anular_venta/<int:pk>/", views.VentaUpdateView.as_view(), name="AnularVenta"),
    path(
        "ventas_anuladas",
        views.VentaAnuladaListView.as_view(),
        name="ListaVentaAnulada",
    ),
    path(
        "ventas_por_cobrar",
        views.VentaPorCobrarListView.as_view(),
        name="VentaPorCobrar",
    )
    # path('usuarios', views.UsuarioListView.as_view(), name = 'Usuarios'),
]
