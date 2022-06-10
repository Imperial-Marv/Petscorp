from distutils import core
from django.contrib import admin
from .models import  Usuario
from .models import  Producto

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)