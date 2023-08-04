from django.contrib import admin

from TEC.models import *

class ConsecionariaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'nombreGerente')
    search_fields = ('nombre', 'direccion')

admin.site.register(Consecionaria, ConsecionariaAdmin)

class ControlEAdmin(admin.ModelAdmin):

    list_display = ('clasificacion','tipo','fecha','mes','expositor','carrera','tema','metodologia','lugar','publico','reporte')
    search_fields = ('clasificacion','tipo')

admin.site.register(ControlE, ControlEAdmin)

class PonentesAdmin(admin.ModelAdmin):

    list_display = ('nombres','area','localidad','foto')
    search_fields = ('nombres','area')

admin.site.register(Ponentes, PonentesAdmin)

class ExpositoresConAdmin(admin.ModelAdmin):

    list_display = ('nombres','apellidos','conocimientos','numEventos','calificacion','presupuesto','correo','telefono','ciudad','contacto')
    search_fields = ('nombres','apellidos')

admin.site.register(ExpositoresCon, ExpositoresConAdmin)

class AutoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'añoFab', 'costoMin', 'costoMax', 'color', 'valorSeguro', 'consecionaria1')
    search_fields = ('marca', 'añoFab')

admin.site.register(Auto, AutoAdmin)

class MotoAdmin(admin.ModelAdmin):

    list_display = ('marcaM', 'añoFabM', 'valorFijo', 'tipo', 'consecionaria2')
    search_fields = ('marcaM', 'tipo')

admin.site.register(Moto, MotoAdmin)