from django.contrib import admin
from .models import PerfilEscola, Fasilidade, Departamento, ProgramaSocio, ProgramaCientifico, ProgramaProdutivo, Autor, Notisia, Categoria, Galeri, AtividadePrincipal, Departamento

class DepartamentoInline(admin.StackedInline):
  model = Departamento
  extra = 1


class PerfilEscolaAdmin(admin.ModelAdmin):
  inlines = [DepartamentoInline]


class NotisiaInline(admin.StackedInline):
  model = Notisia
  extra = 1


class AutorAdmin(admin.ModelAdmin):
  inlines = [NotisiaInline]


admin.site.register(PerfilEscola, PerfilEscolaAdmin)
admin.site.register(Fasilidade)
admin.site.register(AtividadePrincipal)
admin.site.register(ProgramaSocio)
admin.site.register(ProgramaCientifico)
admin.site.register(ProgramaProdutivo)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria)
admin.site.register(Galeri)
admin.site.register(Departamento)