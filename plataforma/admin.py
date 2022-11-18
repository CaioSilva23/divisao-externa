from django.contrib import admin
from .models import Om, Empenho, Fornecedor, Pregao

admin.site.register(Om) 
admin.site.register(Empenho) 
admin.site.register(Fornecedor)
admin.site.register(Pregao)