from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Om
from .forms import OmForms



@login_required(login_url='/auth/logar/') # SÓ TEM ACESSO A HOME, USUÁRIOS LOGADOS
def home(request):

    if request.method == 'POST':
        form_om = OmForms(request.POST, request.FILES)
        if form_om.is_valid:
            form_om.save()
            return HttpResponse("OM SALVA")
    
    elif request.method == 'GET':
        form_om = OmForms()
        return render(request, 'home.html', {'form_om': form_om})
