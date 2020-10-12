from django.contrib import admin

# Register your models here.
from .models import Carrera
from .models import Paralelo

admin.site.register(Carrera)
admin.site.register(Paralelo)
