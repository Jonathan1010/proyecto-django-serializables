from django.urls import path
from . import views

from django.conf.urls import include,url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cliente',views.ClienteViewSet)
router.register(r'producto',views.ProductoViewSet)
router.register(r'proveedor',views.ProveedorViewSet)

urlpatterns = [
    path('',views.index, name='index'),
    url(r'^',include(router.urls)),
    url(r'^api-auth',include('rest_framework.urls',namespace='rest_framework'))
]

