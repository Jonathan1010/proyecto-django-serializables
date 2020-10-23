from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente=models.CharField(max_length=10,default="N/A")
    nombreCliente=models.CharField(max_length=200,default="N/A")
    apellidoCliente=models.CharField(max_length=50,default="N/A")
    numeroCelular=models.IntegerField(default=10)
    direccion=models.CharField(max_length=50,default="N/A")
    

class Producto(models.Model):
    idProducto=models.CharField(max_length=100,default="N/A")
    nombre=models.CharField(max_length=100,default="N/A")
    tipoproducto=models.CharField(max_length=100,default="N/A")
    precio=models.CharField(max_length=100,default="N/A")
    totalcantidad=models.CharField(max_length=100,default="N/A")
    
class Proveedor(models.Model):
    idProveedor=models.CharField(max_length=100,default="N/A")
    nombreProveedor=models.CharField(max_length=200,default="N/A")
    apellidoProveedor=models.CharField(max_length=200,default="N/A")
    numeroCelular=models.IntegerField(default=10)
    direccion=models.CharField(max_length=100,default="N/A")