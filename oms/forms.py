from django import forms
from .models import Om

class OmForms(forms.ModelForm):
    
    class Meta:
        model = Om
        fields = '__all__'

