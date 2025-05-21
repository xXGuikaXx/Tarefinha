from django.contrib import admin
from .models import Medico,Enfermeiros,Pacientes

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome','crm']

@admin.register(Enfermeiros)
class EnfermeirosAdmin(admin.ModelAdmin):
    list_display = ['nome','coren']

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ['nome','sexo']