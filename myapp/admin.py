from django.contrib import admin

# models.
from .models import Proyecto, Unitario

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo_total')

    def costo_total(self, obj):
        unitarios = obj.unitarios.all()

        suma_unitarios = 0 
        for unitario in unitarios: 
            suma_unitarios = suma_unitarios + unitario.costo
        return suma_unitarios
    
class UnitarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo')

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Unitario, UnitarioAdmin)