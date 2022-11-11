from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Om, Empenho
from .forms import OmForms, EmpenhoForms
from django.contrib import messages
from django.contrib.messages import constants
from datetime import date
#


@login_required(login_url='/auth/logar/') 
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
    try:
        om = Om.objects.get(id=id)
        empenhos = Empenho.objects.filter(om_id=id).order_by('numero')
        form_empenho = EmpenhoForms()  
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos, 'form_empenho':form_empenho})
    except:
        form_empenho = EmpenhoForms()    
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos, 'form_empenho':form_empenho})



@login_required(login_url='/auth/logar/')
def inserir_empenho(request, id):
    if request.method == 'POST':
        form_empenho = EmpenhoForms(request.POST, request.FILES)
        if form_empenho.is_valid:
            form_empenho.save()
            messages.add_message(request, constants.SUCCESS, 'Empenho inserido com sucesso')
        return redirect(f'/om_empenhos_id/{id}')

@login_required(login_url='/auth/logar/')
def listar_empenhos(request):
    om_list = Om.objects.all()
    empenhos = Empenho.objects.all().order_by('numero')
    try:
        fornecedor = request.GET.get('fornecedor')
        numero_empenho = request.GET.get('numero_empenho')
        oms = request.GET.get('om_select')

        fornecedor = fornecedor.upper()


        if fornecedor:
            empenhos = Empenho.objects.filter(fornecedor__icontains=fornecedor).order_by('numero')
        if numero_empenho:
            empenhos = Empenho.objects.filter(numero=numero_empenho).order_by('numero')
        if oms:
            empenhos = Empenho.objects.filter(om=oms).order_by('numero')
        return render(request, 'listar_empenhos.html',{'empenhos': empenhos, 'om_list': om_list})
    except:
            return render(request, 'listar_empenhos.html',{'empenhos': empenhos,'om_list': om_list})


@login_required(login_url='/auth/logar/')
def remover_empenho(request, id):
    empenho = Empenho.objects.get(id=id)
    id_om = empenho.om.id
    empenho.delete()
    messages.add_message(request, constants.SUCCESS, 'Empenho deletado com sucesso')
    return redirect(f'/om_empenhos_id/{id_om}')



def deletar_om(request, id):
    om_del = Om.objects.get(id=id)
    om_del.delete()
    messages.add_message(request, constants.SUCCESS, 'OM deletada com sucesso')
    return redirect ('/home/')

def pregoes(request):
    return render(request, 'pregoes.html')