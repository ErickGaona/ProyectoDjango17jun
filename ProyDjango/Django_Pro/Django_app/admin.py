from django.contrib import admin
from Django_app.models import *


class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripción"
    verbose_name_plural = "Inscripciones"


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento', 'instructor')
    search_fields = ('titulo', 'instructor__nombre')
    list_filter = ('departamento', 'instructor')
    inlines = (InscripcionInline,)



# cuando se cree una tarea me de la opcion de agregar entrega

class EntregaInline(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = "Entrega"
    verbose_name_plural = "Entregas"




class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso')
    search_fields = ('titulo',)
    list_filter = ('curso',)
    inlines = (EntregaInline,)




admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Entrega)
admin.site.register(Tarea,TareaAdmin)


