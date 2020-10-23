from django.contrib import admin

# Register your models here.

from .models import Cliente
from .models import Producto
from .models import Proveedor


admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Proveedor)
