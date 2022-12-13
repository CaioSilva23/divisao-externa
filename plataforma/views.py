from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


from .models import Fornecedor, PlanoInterno, NotaCredito, Arquivo
from oms.models import Om
from pregoes.models import Pregao

from django.contrib import messages
from django.contrib.messages import constants
from datetime import date
from django.db.models.aggregates import Avg, Sum, Min, Max
from django.utils.safestring import mark_safe



@login_required(login_url='/auth/logar/') 
def home(request):
    return render(request, 'home.html')


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
    pi = get_object_or_404(PlanoInterno, id=id)
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




 