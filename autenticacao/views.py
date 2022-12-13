from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home_auth(request):

    if request.user.is_authenticated: # VERIFICA SE O USUÁRIO JÁ ESTÁ AUTENTICADOa
        return redirect('home')
    return render(request, 'home_auth.html')



def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated: # VERIFICA SE O USUÁRIO JÁ ESTÁ AUTENTICADO
            return redirect('home')
        return render(request, 'logar.html')

    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=usuario, password=senha) # VERIFICA SE POSSUI O USUÁRIO 

    if not usuario:
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return redirect('/auth/logar')
    else:
        auth.login(request, usuario)  # AUTENTICA O USUÁRIO 
        return redirect('home')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
