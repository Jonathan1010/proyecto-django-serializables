from pruebaapp.models import Cliente,Producto,Proveedor
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields = ('idCliente' , 'nombreCliente' , 'apellidoCliente' , 'numeroCelular' , 'direccion')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields = ('idProducto' , 'nombre' , 'tipoproducto' , 'precio' , 'totalcantidad')

class ProveedorSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Proveedor
        fields=('idProveedor' , 'nombreProveedor' , 'apellidoProveedor' , 'numeroCelular','direccion')