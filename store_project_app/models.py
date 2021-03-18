from django.contrib.auth.models import AbstractUser
from store_project.models import BaseModel
from django.db import models
from django.forms import ModelForm
from django.forms import model_to_dict
from datetime import datetime
from django.conf import settings
from django.db.models.deletion import CASCADE
from crum import get_current_user


class Metodo_Pago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, blank=False)
    nombre = models.CharField(max_length=60, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True, blank=False)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, verbose_name="Cédula")
    nombre = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    telefono = models.CharField(max_length=100, verbose_name="Teléfono")
    correo_electronico = models.CharField(max_length=400, verbose_name="Email")
    genero = models.CharField(
        max_length=10,
        default=None,
        choices=(("M", "Masculino"), ("F", "Femenino")),
        verbose_name="Genero",
    )

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str(self.nombre)


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, blank=False)
    cedula = models.CharField(max_length=12, verbose_name="Cédula")
    nombre = models.CharField(max_length=50, verbose_name="Nombres")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")
    genero = models.CharField(
        max_length=10,
        default=None,
        choices=(("M", "Masculino"), ("F", "Femenino")),
        verbose_name="Genero",
    )

    def __str__(self):
        return str(self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["id_cliente"]


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, blank=True, null=True
    )
    ##id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,blank=True, null=True)
    fecha_venta = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    forma_pago = models.ForeignKey(Metodo_Pago, on_delete=models.CASCADE)
    precio_total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    is_anulada = models.BooleanField(default=False)
    creacion_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="creacion_user",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.id_cliente.nombre

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.creacion_user = user
            else:
                self.actualizacion_usuario = user
        super(Venta, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item["cliente"] = self.id_cliente.toJSON()
        # item['empleado'] = self.creacion_user.toJSON()
        item["forma_pago"] = self.forma_pago.toJSON()
        return item


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
    descripcion = models.CharField(
        max_length=100, verbose_name="Descripción", blank=True, null=True
    )

    def __str__(self):
        return self.nombre

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.creacion_user = user
            else:
                self.actualizacion_usuario = user
        super(Categoria, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["id_categoria"]


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
    stock = models.IntegerField()
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item["categoria"] = self.categoria.toJSON()
        return item

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["id_producto"]


class Detalle_Venta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.id_producto

    def toJSON(self):
        item = model_to_dict(self)
        item["producto"] = self.id_producto.toJSON()
        item["subtotal"] = format(self.subtotal, ".2f")
        return item

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalle de Ventas"
        ordering = ["id_venta"]


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField(default=datetime.now)
    precio_total = models.IntegerField()


class detalle_compra(models.Model):
    id_detalle_compra = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    id_articulo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()


class Historial_Pago(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    monto = models.IntegerField()


# class User(AbstractUser):
#     def toJSON(self):
#         item = model_to_dict(self,exclude=[''])
#         return
