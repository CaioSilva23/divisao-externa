from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from plataforma.models import Fornecedor, NotaCredito, Arquivo
from .models import Om
from empenhos.models import Empenho
from pregoes.models import Pregao

from oms.forms import OmForms
from django.contrib import messages
from django.contrib.messages import constants
from datetime import date



@login_required(login_url='/auth/logar/')
def home_oms(request):
    if request.method == 'POST':
        form_om = OmForms(request.POST, request.FILES)

        if form_om.is_valid():
            form_om.save()
            messages.add_message(request, constants.SUCCESS, 'OM cadastrada com sucesso')
            return redirect('/home_oms/')
            
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao inserir OM, dados inválidos!')
            return redirect('/home_oms/')
    
    elif request.method == 'GET':
        form_om = OmForms()
        oms = Om.objects.all()
        return render(request, 'home_oms.html', {'form_om': form_om, 'oms': oms})

@login_required(login_url='/auth/logar/')
def dados_om_id(request, id):
    if request.method == 'GET':
        om = get_object_or_404(Om,id=id)
        arq = Arquivo.objects.filter(om_id=id)
        data = date.today()
        return render(request, 'dados_om.html',{'om':om, 'arq': arq, 'data':data})

@login_required(login_url='/auth/logar/')
def om_empenhos(request):
    if request.method == 'GET':
        oms = Om.objects.all()
        return render(request, 'om_empenhos.html',{'oms':oms})

@login_required(login_url='/auth/logar/')
def om_empenhos_id(request, id):
    fornecedor = Fornecedor.objects.all()
    om = get_object_or_404(Om, id=id)
    pregoes = Pregao.objects.all()
    nc = NotaCredito.objects.all()
    
    empenhos = Empenho.objects.filter(om_id=id)
    
    try:
        fornecedor_filtar = request.GET.get('fornecedor')
        numero_empenho_filtar = request.GET.get('numero_empenho')
        if fornecedor_filtar:
            empenhos = Empenho.objects.filter(fornecedor__icontains=fornecedor_filtar)
            empenhos = empenhos.filter(om_id=id)

        if numero_empenho_filtar:
            empenhos = Empenho.objects.filter(numero=numero_empenho_filtar).order_by('numero')
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos, 'fornecedor': fornecedor,'pregoes':pregoes, 'nc': nc})
    except:
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos,  'fornecedor': fornecedor,'pregoes':pregoes, 'nc': nc})

@login_required(login_url='/auth/logar/') 
def deletar_om(request, id):
    om_del = Om.objects.get(id=id)
    om_del.delete()
    messages.add_message(request, constants.SUCCESS, 'OM deletada com sucesso')
    return redirect ('/home_oms/')
