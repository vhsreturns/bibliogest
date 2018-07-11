from django.contrib import admin

from .models import Prestamo, Usuario, Libro, LugarPrestamo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(LugarPrestamo)