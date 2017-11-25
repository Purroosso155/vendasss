# -*- coding: utf-8 -*
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login

def mensagem(request):return render_to_response('mensagem.html',
         context_instance=RequestContext(request),)

def cadastrar(request):
    titulo = 'Cadastro de Usuários'
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/bemvindo/')
    else:
        form = FormRegistro()
    return render_to_response(
        'cadastrar.html',
        locals(),
         context_instance=RequestContext(request),
)


@login_required
def bemvindo(request):
    return render_to_response('bem_vindo.html',locals(),
         context_instance=RequestContext(request),)

@login_required
def contato(request):
    titulo='ENVIE NOS SUA OPINIÃO SUGESTÃO OU CRÍTICA'
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            #return HttpResponseRedirect('/contatoenviado/')

    else:
        form = FormContato()
    return render_to_response(
    'cadastro.html',
    locals(),
    context_instance=RequestContext(request),
)

@login_required
def contatoenviado(request):return render_to_response('contatoenviado.html',
         context_instance=RequestContext(request))