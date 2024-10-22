from django.contrib import admin
from .models import Perfil, Animalito

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'cedula', 'telefono', 'rol', 'email')
    search_fields = ('cedula', 'telefono', 'user__username', 'email')
    list_filter = ('rol',)

class AnimalitoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'descripcion', 'imagen','estado', 'ayudador_nombre', 'ayudador_telefono')

    def ayudador_nombre(self, obj):
        return obj.ayudador.user.username 

    def ayudador_telefono(self, obj):
        return obj.ayudador.telefono

    ayudador_nombre.short_description = 'Nombre del Ayudador'
    ayudador_telefono.short_description = 'Teléfono del Ayudador'

class VeteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  
    search_fields = ('nombre',)


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Animalito, AnimalitoAdmin)

