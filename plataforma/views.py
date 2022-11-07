from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Om, Empenho
from .forms import OmForms, EmpenhoForms
from django.contrib import messages
from django.contrib.messages import constants



@login_required(login_url='/auth/logar/') # SÓ TEM ACESSO A HOME, USUÁRIOS LOGADOS
def home(request):
    if request.method == 'POST':
        form_om = OmForms(request.POST, request.FILES)
        if form_om.is_valid:
            form_om.save()
            messages.add_message(request, constants.SUCCESS, 'OM cadastrada com sucesso')
            return redirect('/home/')
    
    elif request.method == 'GET':
        form_om = OmForms()
        oms = Om.objects.all()
        return render(request, 'home.html', {'form_om': form_om, 'oms': oms})


@login_required(login_url='/auth/logar/')
def dados_om_id(request, id):
    om = Om.objects.filter(id=id)
    return render(request, 'dados_om.html',{'om':om})


@login_required(login_url='/auth/logar/')
def om_empenhos(request):
    oms = Om.objects.all()
    return render(request, 'om_empenhos.html',{'oms':oms})


@login_required(login_url='/auth/logar/')
def om_empenhos_id(request, id):
    om = Om.objects.filter(id=id)
    empenhos = Empenho.objects.filter(om_id=id)
    form_empenho = EmpenhoForms()
    return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos, 'form_empenho':form_empenho})


@login_required(login_url='/auth/logar/')
def inserir_empenho(request, id):
    if request.method == 'POST':
        form_empenho = EmpenhoForms(request.POST, request.FILES)
        if form_empenho.is_valid:
            form_empenho.save()
        return redirect(f'/om_empenhos_id/{id}')


def remover_empenho(request, id):
    pass

