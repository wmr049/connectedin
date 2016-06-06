from django.shortcuts import render,redirect
from perfis.models import Perfil

def index(request):
	return render(request, 'index.html',{'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})

def exibir(request,perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)

	return render(request,'perfil.html', {"perfil" : perfil})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfi_logado = get_perfil_logado(request)
	perfi_logado.convidar(perfil_a_convidar)

	return redirect('index')


def get_perfil_logado(request):
	return Perfil.objects.get(id=1)