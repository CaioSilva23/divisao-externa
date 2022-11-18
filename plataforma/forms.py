from django import forms
from .models import Om, Empenho

class OmForms(forms.ModelForm):
    
    class Meta:
        model = Om
        fields = ('sigla','foto', 'email', 'telefone')

#ch_almox','tel_ch_almox','adj_almox','tel_adj_almox'
