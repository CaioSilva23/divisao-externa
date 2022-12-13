from django.contrib import admin
from .models import Fornecedor, PlanoInterno, NotaCredito, Arquivo

# admin.site.register(Om) 

admin.site.register(Fornecedor)
admin.site.register(PlanoInterno)
admin.site.register(NotaCredito)
admin.site.register(Arquivo)