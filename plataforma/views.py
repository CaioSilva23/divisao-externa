from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Om, Empenho, Fornecedor, Pregao, PlanoInterno, NotaCredito, Arquivo
from .forms import OmForms
from django.contrib import messages
from django.contrib.messages import constants
from datetime import date
from django.db.models.aggregates import Avg, Sum, Min, Max
from .entidade import tabela

def home_auth(request):

    if request.user.is_authenticated: # VERIFICA SE O USUÁRIO JÁ ESTÁ AUTENTICADOa
        return redirect('home')
    return render(request, 'home_auth.html')


@login_required(login_url='/auth/logar/') 
def home(request):
    nc_credito = NotaCredito.objects.get(id=1)
    a = nc_credito.disponivel()
    print(type(a))
    return render(request, 'home.html')

def home_oms(request):
    
    if request.method == 'POST':
        form_om = OmForms(request.POST, request.FILES)
        if form_om.is_valid:
            form_om.save()
            messages.add_message(request, constants.SUCCESS, 'OM cadastrada com sucesso')
            return redirect('/home_oms/')
    
    elif request.method == 'GET':
        form_om = OmForms()
        oms = Om.objects.all()
        return render(request, 'home_oms.html', {'form_om': form_om, 'oms': oms})


@login_required(login_url='/auth/logar/')
def dados_om_id(request, id):
    oms = Om.objects.all()
    om = Om.objects.get(id=id)
    arq = Arquivo.objects.filter(om_id=id)
    data = date.today()
    return render(request, 'dados_om.html',{'om':om, 'arq': arq, 'oms': oms, 'data':data})


@login_required(login_url='/auth/logar/')
def om_empenhos(request):
    oms = Om.objects.all()
    return render(request, 'om_empenhos.html',{'oms':oms})


@login_required(login_url='/auth/logar/')
def om_empenhos_id(request, id):
    fornecedor = Fornecedor.objects.all()
    om = get_object_or_404(Om, id=id)
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
        print(data)
     
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

        forn1 = Fornecedor.objects.get(id=fornecedor)
        om_id = Om.objects.get(id=om)

        pregao_id = Pregao.objects.get(id=pregao)

        nc_credito = NotaCredito.objects.get(id=nc)
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
    valor= request.POST.get('valor')

    print(oms)
    try:
        novo_pregao = Pregao(pregao=pregao,
                            situacao=situacao,
                            termo_homolocao=link,
                            descrição=descricao,
                            catalago=catalogo,
                            saldo_homologado=valor)
        novo_pregao.save()
        novo_pregao.oms_favorecidas.add(*oms)
        novo_pregao.save()


        messages.add_message(request, constants.SUCCESS, 'Pregão inserido com sucesso')
        return redirect ('/pregoes/')
    except Exception as e:
     
        messages.add_message(request, constants.ERROR, 'Erro ao inserir o pregão')
        return redirect ('/pregoes/')

@login_required(login_url='/auth/logar/') 
def deletar_pregao(request, id):
    pregao = Pregao.objects.get(id=id)
    pregao.delete()
    messages.add_message(request, constants.SUCCESS, 'Pregão deletado com sucesso')
    return redirect ('/pregoes/')


def capacidade_empenho(request, id):
    pregao = Pregao.objects.get(id=id)

    
    empenhado = Empenho.objects.filter(pregao_id=id).aggregate(Sum('valor'))
    if empenhado['valor__sum']:
        empenhado = empenhado['valor__sum'] 
    else:
        empenhado = 0

    try:
        inicial = float(pregao.saldo_homologado)
        final = float(empenhado)
        soma = inicial + final
        capacidade = f'{inicial - empenhado:_.2f}'.replace('.',',').replace('_','.')
        r = (soma - inicial) / inicial * 100
    
        r = '{:.2f}'.format(r)

        empenhado = f'{empenhado:_.2f}'.replace('.',',').replace('_','.')

        # saldo = f'{self.valor:_.2f}'
        # return saldo.replace('.',',').replace('_','.')
    except Exception as e:
        pass
    return render(request, 'capacidade_empenho.html', {'pregao':pregao, 'empenhado': empenhado, 'r':r, 'capacidade': capacidade})

# API DASHBOARD
def dashboard(request):
    pregao = Pregao.objects.all()
    homologado = []
    l_empenhado = []
    p = []
    percent = []
    for i in pregao:
        empenhado = Empenho.objects.filter(pregao_id=i.id).aggregate(Sum('valor'))
        if empenhado['valor__sum']:
            empenhado = empenhado['valor__sum'] 
        else:
            empenhado = 0

        try:
            inicial = float(i.saldo_homologado)
            final = float(empenhado)

            soma = inicial + final
            capacidade = inicial - empenhado
            r = (soma - inicial) / inicial * 100
            
            r = '{:.2f}'.format(r)
            
        except Exception as e:
            
            pass
            # print(e)homologado
        homologado.append(i.saldo_homologado)
        l_empenhado.append(empenhado)
        p.append(i.pregao)
        percent.append(r)
    x = {'labels': p, 'data':percent}
    return JsonResponse(x)


def homologado(request):
    homologado = Pregao.objects.all().aggregate(Sum('saldo_homologado'))['saldo_homologado__sum']
    if not homologado:
        homologado = 0
    homologado = f'{homologado:_.2f}'
    homologado = homologado.replace('.',',').replace('_','.')

    return JsonResponse({'homologado':homologado})

def empenhado(request):
    empenhado = Empenho.objects.all().aggregate(Sum('valor'))['valor__sum']
    if not empenhado:
        empenhado = 0


    empenhado = f'R$ {empenhado:_.2f}'
    empenhado = empenhado.replace('.',',').replace('_','.')
    return JsonResponse({'empenhado':empenhado})

def capacidade(request):
    empenhado = Empenho.objects.all().aggregate(Sum('valor'))['valor__sum']
    homologado = Pregao.objects.all().aggregate(Sum('saldo_homologado'))['saldo_homologado__sum']
    if not empenhado:
        empenhado = 0
    if not homologado:
        homologado = 0
    capacidade = homologado - empenhado

    capacidade = f'{capacidade:_.2f}'
    capacidade = capacidade.replace('.',',').replace('_','.')
    return JsonResponse({'capacidade':capacidade})

def home_tabela(request):
    pregao = Pregao.objects.all()
    lista = []
    for i in pregao:
        empenhado = Empenho.objects.filter(pregao_id=i.id).aggregate(Sum('valor'))
        if empenhado['valor__sum']:
            empenhado = empenhado['valor__sum'] 
        else:
            empenhado = 0

        try:
            inicial = float(i.saldo_homologado)
            final = float(empenhado)

            soma = inicial + final
            capacidade = inicial - empenhado
            r = (soma - inicial) / inicial * 100
            
            r = '{:.2f}'.format(r)
            
        except Exception as e:
            print(e)
            pass
            # print(e)homologado

        n = tabela.Tabela(i, empenhado, capacidade, r)
        lista.append(n)

    print(lista)

    return render(request, 'home_tabela.html', {'lista':lista})

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

    # nc = NotaCredito.objects.all()
    # for n in nc:
    #     print(n.numero ,n.saldo_empenhado())
    for c in creditos:
        print(c.id)


    return render(request, 'credito.html',{'creditos': creditos} )

def nc(request, id):
    nc = NotaCredito.objects.filter(pi_id=id)
    pi = PlanoInterno.objects.get(id=id)
    return render(request, 'nc.html',{'nc':nc, 'pi':pi})



def inserir_demanda(request):
    
    try:
        om = request.POST.get('om')
        demanda = request.FILES.get('demanda')
        data = date.today()


        om_id = Om.objects.get(id=om)

        novo_arquivo = Arquivo(om=om_id,
                                demanda=demanda,
                                data=data)

        novo_arquivo.save()
        messages.add_message(request, constants.SUCCESS, 'DOCUMENTOS ENVIADOS')

        return redirect(f'/dados_om/{om}/')
    except Exception as e:
        print(e)
        messages.add_message(request, constants.ERROR, 'ERRO, TENTE NOVAMENTE')
        return redirect(f'/dados_om/{om}/')




 