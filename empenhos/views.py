from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Empenho
from plataforma.models import NotaCredito, Fornecedor
from oms.models import Om
from pregoes.models import Pregao
from django.contrib import messages
from django.contrib.messages import constants





@login_required(login_url='/auth/logar/')
def inserir_empenho(request, id):
    if request.method == 'GET':
        return redirect(f'/om_empenhos_id/{id}')
        
    if request.method == 'POST':
        om = request.POST.get('om')
        fornecedor = request.POST.get('fornecedor')
        numero_empenho = request.POST.get('numero_empenho')
        pregao = request.POST.get('pregao')
        data = request.POST.get('data')
        pdf = request.FILES.get('pdf')
        valor = request.POST.get('valor')
        nc = request.POST.get('nc')
      
     
        if ( len(om.strip()) == 0 or len(fornecedor.strip()) == 0 or len(numero_empenho.strip()) == 0 or len(pregao.strip()) ==0 or len(data.strip()) ==0): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect(f'/om_empenhos_id/{id}')

        if not numero_empenho.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite o número do empenho válido')
            return redirect(f'/om_empenhos_id/{id}')
            
        if not pregao.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite um pregão válido (sem / )')
            return redirect(f'/om_empenhos_id/{id}')

        empenho = Empenho.objects.filter(numero=numero_empenho)
        
        if empenho.exists():
            messages.add_message(request, constants.ERROR, 'Empenho já existe')
            return redirect(f'/om_empenhos_id/{id}')

        # if pdf.size > 100_000_000:
        #     messages.add_message(request, constants.ERROR, 'PDF não pode ser mair que 10MB')
        #     return redirect(f'/om_empenhos_id/{id}')

        forn1 = get_object_or_404(Fornecedor, id=fornecedor)
        om_id = get_object_or_404(Om, id=om)

        pregao_id = get_object_or_404(Pregao, id=pregao)

        nc_credito = get_object_or_404(NotaCredito, id=nc)
        a = nc_credito.disponivel().replace('.','').replace(',','.')

        if float(a) < float(valor):



            messages.add_message(request, constants.ERROR, 'SALDO DA NOTA DE CRÉDITO INSUFICIENTE')
            return redirect(f'/om_empenhos_id/{id}')
        try:
            empenho = Empenho(om=om_id,
                                fornecedor=forn1,
                                pregao=pregao_id,
                                data=data,
                                numero=numero_empenho,
                                pdf=pdf, 
                                valor=valor,
                                nota_credito=nc_credito)
            empenho.save()
        
            messages.add_message(request, constants.SUCCESS, 'Empenho inserido com sucesso')
            return redirect(f'/om_empenhos_id/{id}')
        except Exception as e:
            
            messages.add_message(request, constants.ERROR, 'ERRO AO INSERIR EMPENHO')
            return redirect(f'/om_empenhos_id/{id}')

@login_required(login_url='/auth/logar/')
def listar_empenhos(request):
    fornecedor = request.GET.get('fornecedor')
    numero_empenho = request.GET.get('numero_empenho')
    om_filtrar = request.GET.get('om_select')

    om_list = Om.objects.all()
    empenhos = Empenho.objects.all().order_by('numero')
    fornecedores_list = Fornecedor.objects.all()
    try:
        print(fornecedor)
        if fornecedor:
            empenhos = empenhos.filter(fornecedor=fornecedor).order_by('numero')
        if numero_empenho:
            empenhos = empenhos.filter(numero=numero_empenho).order_by('numero')
        if om_filtrar:
            empenhos = empenhos.filter(om=om_filtrar).order_by('numero')

        return render(request, 'listar_empenhos.html',{'empenhos': empenhos, 'om_list': om_list, 'fornecedores_list': fornecedores_list})
    except:
        return render(request, 'listar_empenhos.html',{'empenhos': empenhos,'om_list': om_list, 'fornecedores_list': fornecedores_list})

@login_required(login_url='/auth/logar/')
def remover_empenho(request, id):
    empenho = Empenho.objects.get(id=id)
    id_om = empenho.om.id
    empenho.delete()
    messages.add_message(request, constants.SUCCESS, 'Empenho deletado com sucesso')
    return redirect(f'/om_empenhos_id/{id_om}')

@login_required(login_url='/auth/logar/')
def entregue(request, id):
    empenho = Empenho.objects.filter(id=id)
    if not empenho.exists():
        messages.add_message(request, constants.ERROR, 'Delete apenas empenhos válidos!')
        return redirect('/home/')
    

    empenho = empenho.first()
    if empenho.entregue == True:
        messages.add_message(request, constants.ERROR, 'Registro de entrega já foi realizado para este empenho!')
        return redirect(f'/om_empenhos_id/{empenho.om.id}')
    elif empenho.entregue == False:
        empenho.entregue = True
        empenho.save()
        messages.add_message(request, constants.SUCCESS, 'Registro de entrega realizado!')
        return redirect(f'/om_empenhos_id/{empenho.om.id}')