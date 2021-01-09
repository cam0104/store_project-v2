from django.db import models
from django.forms import ModelForm

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True,blank=False)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=400)

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, blank=False)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    id_empleado = models.ForeignKey('Empleado',on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    forma_pago = models.ForeignKey('Metodo_Pago',on_delete=models.CASCADE)
    precio_total = models.IntegerField()
    
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True,blank=False)
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

class Detalle_Venta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta',on_delete=models.CASCADE)
    id_producto = models.ForeignKey
    cantidad = models.IntegerField()
    precio = models.IntegerField()

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    precio_total =  models.IntegerField()

class detalle_compra(models.Model):
    id_detalle_compra = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey('Compra',on_delete=models.CASCADE)  
    id_articulo = models.ForeignKey('Producto',on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.IntegerField()
    fecha_vencimiento = models.DateTimeField(blank=True,null=True)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Metodo_Pago(models.Model):
    id_metodo_pago = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Historial_Pago(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    monto = models.IntegerField()
