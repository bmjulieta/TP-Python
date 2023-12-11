from django.contrib import admin

# Register your models here.
from .models import Servicio, MetodoDeCobro, MetodoDePago, Categoria, Producto, Cliente, Blog, Contacto, ServicioB, AboutUs

#Register your models here.
admin.site.register(Servicio)
admin.site.register(MetodoDeCobro)
admin.site.register(MetodoDePago)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Blog)
admin.site.register(Contacto)
admin.site.register(ServicioB)
admin.site.register(AboutUs)