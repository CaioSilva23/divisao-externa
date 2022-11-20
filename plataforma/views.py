from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Om, Empenho, Fornecedor, Pregao, PlanoInterno, NotaCredito, Arquivo
from .forms import OmForms
from django.contrib import messages
from django.contrib.messages import constants

def home_auth(request):
    if request.user.is_authenticated: # VERIFICA SE O USUÁRIO JÁ ESTÁ AUTENTICADO
        return redirect('home')
    return render(request, 'home_auth.html')


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
    oms = Om.objects.all()
    om = Om.objects.get(id=id)
    arq = Arquivo.objects.filter(om_id=id)
    return render(request, 'dados_om.html',{'om':om, 'arq': arq, 'oms': oms})


@login_required(login_url='/auth/logar/')
def om_empenhos(request):
    oms = Om.objects.all()
    return render(request, 'om_empenhos.html',{'oms':oms})


@login_required(login_url='/auth/logar/')
def om_empenhos_id(request, id):
    fornecedor = Fornecedor.objects.all()
    om = Om.objects.get(id=id)
    empenhos = Empenho.objects.filter(om_id=id).order_by('numero')
    pregoes = Pregao.objects.all()
    nc = NotaCredito.objects.all()
    
    try:
        fornecedor_filtar = request.GET.get('fornecedor')
        numero_empenho_filtar = request.GET.get('numero_empenho')
        if fornecedor_filtar:
            empenhos = Empenho.objects.filter(fornecedor__icontains=fornecedor_filtar).order_by('numero')
            empenhos = empenhos.filter(om_id=id).order_by('numero')

        if numero_empenho_filtar:
            empenhos = Empenho.objects.filter(numero=numero_empenho_filtar)
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos, 'fornecedor': fornecedor,'pregoes':pregoes, 'nc': nc})
    except:
        return render(request, 'om_empenhos_id.html',{'om':om, 'empenhos':empenhos,  'fornecedor': fornecedor,'pregoes':pregoes, 'nc': nc})


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

        if pdf.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'PDF não pode ser mair que 10MB')
            return redirect(f'/om_empenhos_id/{id}')

        forn1 = Fornecedor.objects.get(id=fornecedor)
        om_id = Om.objects.get(id=om)
        pregao_id = Pregao.objects.get(id=pregao)
        nc_credito = NotaCredito.objects.get(id=nc)
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
            
            nova_nc = NotaCredito.objects.get(id=nc)

            nova_nc.valor -= float(valor)
            nova_nc.save()


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
def deletar_om(request, id):
    om_del = Om.objects.get(id=id)
    om_del.delete()
    messages.add_message(request, constants.SUCCESS, 'OM deletada com sucesso')
    return redirect ('/home/')

@login_required(login_url='/auth/logar/') 
def pregoes(request):
    pregoes = Pregao.objects.all()
    oms = Om.objects.all()
    return render(request, 'pregoes.html', {'pregoes': pregoes, 'oms': oms})

@login_required(login_url='/auth/logar/') 
def inserir_pregao(request):
    pregao = request.POST.get('pregao')
    descricao = request.POST.get('descricao')
    situacao = request.POST.get('situacao')
    oms = request.POST.getlist('oms')
    link = request.POST.get('link')
    catalogo = request.FILES.get('catalogo')

    print(oms)
    try:
        novo_pregao = Pregao(pregao=pregao,
                            situacao=situacao,
                            termo_homolocao=link,
                            descrição=descricao,
                            catalago=catalogo)
        novo_pregao.save()
        novo_pregao.oms_favorecidas.add(*oms)
        novo_pregao.save()


        messages.add_message(request, constants.SUCCESS, 'Pregão inserido com sucesso')
        return redirect ('/pregoes/')
    except Exception as e:
        print(e)
        messages.add_message(request, constants.ERROR, 'Erro ao inserir o pregão')
        return redirect ('/pregoes/')

@login_required(login_url='/auth/logar/') 
def deletar_pregao(request, id):
    pregao = Pregao.objects.get(id=id)
    pregao.delete()
    messages.add_message(request, constants.SUCCESS, 'Pregão deletado com sucesso')
    return redirect ('/pregoes/')

@login_required(login_url='/auth/logar/') 
def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    
    nome = request.GET.get('nome')

    if nome:
        fornecedores = fornecedores.filter(nome__contains=nome)

    return render(request, 'fornecedores.html', {'fornecedores': fornecedores})

@login_required(login_url='/auth/logar/') 
def inserir_fornecedor(request):
    if request.method == 'GET':
        return redirect('fornecedores/')
    elif request.method == 'POST':
        nome = request.POST.get('nome').upper()
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        telefone = request.POST.get('email')

        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(telefone.strip()) == 0 or len(email.strip()) ==0): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/fornecedores/')

        if not cnpj.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite cnpj válido')
            return redirect('/fornecedores/')
            
        # if not telefone.isnumeric():
        #     messages.add_message(request, constants.ERROR, 'Digite telefone válido')
        #     return redirect('/fornecedores/')

        fornecedor = Fornecedor.objects.filter(cnpj=cnpj)
        
        if fornecedor.exists():
            messages.add_message(request, constants.ERROR, 'Fornecedor já existe')
            return redirect('/fornecedores/')

        try:
            novo_fornecedor = Fornecedor(nome=nome, cnpj=cnpj, email=email, telefone=telefone)
            novo_fornecedor.save()
            messages.add_message(request, constants.SUCCESS, 'Fornecedor inserido com sucesso')
            return redirect('/fornecedores/')
        except Exception as e:
            print(e)
            messages.add_message(request, constants.ERROR, 'Erro ao inserir o fornecedor')
            return redirect('/fornecedores/')

@login_required(login_url='/auth/logar/') 
def deletar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    fornecedor.delete()
    return redirect('/fornecedores/')



def credito(request):
    creditos = PlanoInterno.objects.all()


    # for emp in empenhados:
    #     print(emp.saldo_empenhado())'empenhados': empenhados
    return render(request, 'credito.html',{'creditos': creditos} )



def inserir_demanda(request):
    om = request.POST.get('om')
    demanda = request.FILES.get('demanda')
    data = request.POST.get('data')


    om_id = Om.objects.get(id=om)

    novo_arquivo = Arquivo(om=om_id,
                            demanda=demanda,
                            data=data)

    novo_arquivo.save()
    messages.add_message(request, constants.SUCCESS, 'DOCUMENTOS ENVIADOS')

    return redirect(f'/dados_om/{om}/')




 