from django.contrib import admin
from .models import Om, Empenho, Fornecedor, Pregao, PlanoInterno, NotaCredito, Arquivo

admin.site.register(Om) 
admin.site.register(Empenho) 
admin.site.register(Fornecedor)
admin.site.register(Pregao)
admin.site.register(PlanoInterno)
admin.site.register(NotaCredito)
admin.site.register(Arquivo)