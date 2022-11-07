from django import forms
from .models import Om, Empenho

class OmForms(forms.ModelForm):
    
    class Meta:
        model = Om
        fields = ('sigla','foto', 'email', 'telefone')


class EmpenhoForms(forms.ModelForm):
    
    class Meta:
        model = Empenho
        fields = ('om','fornecedor', 'nd', 'ug','pregao','data', 'numero', 'pdf')

