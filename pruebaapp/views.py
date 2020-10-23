# Create your views here.
from django.http import HttpResponse

from pruebaapp.models import Cliente,Producto,Proveedor
from rest_framework import viewsets
from pruebaapp.serializers import ClienteSerializer,ProductoSerializer,ProveedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset=Cliente.objects.all().order_by('nombreCliente')
    serializer_class=ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all().order_by('nombre')
    serializer_class=ProductoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset=Proveedor.objects.all().order_by('nombreProveedor')
    serializer_class=ProveedorSerializer

def index(request):
    return HttpResponse("En esta aplicacion se vendran productos de buena calidad sin riesgo a contagio del Covid")