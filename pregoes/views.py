from django.shortcuts import render, redirect , get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# IMPORTAÇÕES DAS MODELS
from .models import Pregao
from oms.models import Om
from empenhos.models import Empenho


from django.contrib import messages
from django.contrib.messages import constants

from django.db.models.aggregates import Avg, Sum, Min, Max

from .entidade import tabela
from django.utils.safestring import mark_safe



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
    empenhado = Empenho.objects.filter(pregao_id=id).aggregate(Sum('valor'))['valor__sum']

    if not empenhado:
        empenhado = 0
    try:
        # CAPACIDADE DE EMPENHO
        inicial = float(pregao.saldo_homologado)
        final = float(empenhado)
        capacidade = f'{inicial - empenhado:_.2f}'.replace('.',',').replace('_','.')
        
        # PORCENTAGEM EMPENHADO DO PREGAO
        soma = inicial + final
        r = (soma - inicial) / inicial * 100
        r = '{:.2f}'.format(r)
        
        # SALDO EMPENHADO DO PREGAO
        empenhado = f'{empenhado:_.2f}'.replace('.',',').replace('_','.')
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
        empenhado = Empenho.objects.filter(pregao_id=i.id).aggregate(Sum('valor'))['valor__sum']
        if not empenhado:
            empenhado = 0
        try:
            inicial = float(i.saldo_homologado)
            final = float(empenhado)
            soma = inicial + final
            r = (soma - inicial) / inicial * 100
            r = '{:.2f}'.format(r)
            
        except Exception as e:
            pass
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
        if True:
            if float(r) < 50:
                classe = "table-danger"
            elif float(r) >= 50 and float(r) < 70:
                classe = "table-warning"
            elif float(r) > 70:
                classe = "table-success"

            prioridade = f'''class="{classe}"'''

        prioridade = mark_safe(str(prioridade))    
        n = tabela.Tabela(i, empenhado, capacidade, r, prioridade)
        lista.append(n)



    return render(request, 'home_tabela.html', {'lista':lista})
