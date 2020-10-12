# Create your views here.
from django.http import HttpResponse

from pruebaapp.models import Carrera,Paralelo
from rest_framework import viewsets
from pruebaapp.serializers import CarreraSerializer,ParaleloSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset=Carrera.objects.all().order_by('nombreCarrera')
    serializer_class=CarreraSerializer

class ParaleloViewSet(viewsets.ModelViewSet):
    queryset=Paralelo.objects.all().order_by('nombre')
    serializer_class=ParaleloSerializer

def index(request):
    return HttpResponse("Hola mundo, es mi primera app de prueba en Django soy Jonathan Buri")