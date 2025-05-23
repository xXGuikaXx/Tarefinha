from django.contrib import admin
from .models import Medico,Enfermeiros,Pacientes,Especialidade
from .utils import get_idade

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    ordering = ['nome']

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome','crm']
    filter_horizontal = ['especialidade']

@admin.register(Enfermeiros)
class EnfermeirosAdmin(admin.ModelAdmin):
    list_display = ['nome','coren']

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ['nome','sexo']