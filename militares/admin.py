from django.contrib import admin
from .models import Soldado, Cuartel, Servicio, Cuerpos_del_ejercito, Compañia, Soldados_registrado

class SoldadoAdmin(admin.ModelAdmin):
    fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'graduacion']
    list_display = ('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'graduacion')
    search_fields = ['primer_nombre','segundo_nombre', 'primer_apellido', 'segundo_apellido']

admin.site.register(Soldado, SoldadoAdmin)
admin.site.register(Cuartel)
admin.site.register(Servicio)
admin.site.register(Cuerpos_del_ejercito)
admin.site.register(Compañia)
admin.site.register(Soldados_registrado)
# Register your models here.
