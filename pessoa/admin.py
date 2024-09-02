from django.contrib import admin
from .models import Pessoas, Conjuge, Dependentes

class PessoasAdmin(admin.ModelAdmin):
    exclude = ('idade',)  # Exclui o campo 'idade'

class ConjugeAdmin(admin.ModelAdmin):
    exclude = ('idade',)  # Exclui o campo 'idade'

class DependentesAdmin(admin.ModelAdmin):
    exclude = ('idade',)  # Exclui o campo 'idade'

admin.site.register(Pessoas, PessoasAdmin)
admin.site.register(Conjuge, ConjugeAdmin)
admin.site.register(Dependentes, DependentesAdmin)
