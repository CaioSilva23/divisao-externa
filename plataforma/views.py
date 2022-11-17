from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Om, Empenho, Fornecedor
from .forms import OmForms
from django.contrib import messages
from django.contrib.messages import constants

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
    fornecedor = Fornecedor.objects.all()
    om = Om.objects.get(id=id)
    empenhos = Empenho.objects.filter(om_id=id).order_by('numero')
    
    try:
        fornecedor_filtar = request.GET.get('fornecedor')
        numero_empenho_filtar = request.GET.get('numero_empenho')
        if fornecedor_filtar:
            empenhos = Empenho.objects.filter(fornecedor__icontains=fornecedor_filtar).order_by('numero')
            empenhos = empenhos.filter(om_id=id).order_by('numero')

        if numero_empenho_filtar:
            empenhos = Empenho.objects.filter(numero=numero_empenho_filtar)
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos, 'fornecedor': fornecedor})
    except:
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos,  'fornecedor': fornecedor})



@login_required(login_url='/auth/logar/')
def inserir_empenho(request, id):
    if request.method == 'GET':
        return redirect(f'/om_empenhos_id/{id}')
        
    if request.method == 'POST':
        om1 = request.POST.get('om')
        fornecedor1 = request.POST.get('fornecedor')
        numero_empenho1 = request.POST.get('numero_empenho')
        nd1 = request.POST.get('nd')
        ug1 = request.POST.get('ug')
        pregao1 = request.POST.get('pregao')
        data1 = request.POST.get('data')
        pdf1 = request.FILES.get('pdf')
     

        forn1 = Fornecedor.objects.get(id=fornecedor1)
        om_id = Om.objects.get(id=om1)

        try:
            empenho = Empenho(om=om_id,
                                fornecedor=forn1,
                                nd=nd1,ug=ug1,
                                pregao=pregao1,
                                data=data1,
                                numero=numero_empenho1,
                                pdf=pdf1)
            empenho.save()
            messages.add_message(request, constants.SUCCESS, 'Empenho inserido com sucesso')
            return redirect(f'/om_empenhos_id/{id}')
        except Exception as e:
            print(e)
            messages.add_message(request, constants.ERROR, 'ERRO AO INSERIR EMPENHO')
            return redirect(f'/om_empenhos_id/{id}')





@login_required(login_url='/auth/logar/')
def listar_empenhos(request):
    fornecedor = request.GET.get('fornecedor')
    numero_empenho = request.GET.get('numero_empenho')


    om_list = Om.objects.all()
    empenhos = Empenho.objects.all().order_by('numero')
    try:

        # om_filtrar = request.GET.get('om_select')

       

        print(fornecedor)
        if fornecedor:
            empenhos = empenhos.filter(fornecedor=fornecedor).order_by('numero')
            return render(request, 'listar_empenhos.html',{'empenhos': empenhos, 'om_list': om_list})
        if numero_empenho:
            empenhos = empenhos.filter(numero=numero_empenho).order_by('numero')
        # if om_filtrar:
        #     empenhos = Empenho.objects.filter(om=om_filtrar).order_by('numero')

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


@login_required(login_url='/auth/logar/') 
def deletar_om(request, id):
    om_del = Om.objects.get(id=id)
    om_del.delete()
    messages.add_message(request, constants.SUCCESS, 'OM deletada com sucesso')
    return redirect ('/home/')

@login_required(login_url='/auth/logar/') 
def pregoes(request):
    return render(request, 'pregoes.html')

def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores.html', {'fornecedores': fornecedores})