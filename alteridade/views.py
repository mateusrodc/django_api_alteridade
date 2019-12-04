from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/index')
    return render(request, 'login.html')

def do_logout(request):
	logout(request)
	return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html', context={})
@login_required
def listaStatus(request):
    stats= Status.objects.all()
    return render(request,'listaStatus.html',context={'stats': stats})
@login_required
def adicionarStatus(request):
    return render(request,'adicionarStatus.html',context=None)
@login_required
def salvarStatus(request):
    situacao= request.POST.get('situacao')
    id_stats= request.POST.get('id_stats')

    if id_stats:
        statss= Status.objects.get(pk=id_stats)
    else:
        statss= Status()

    statss.situacao=situacao
    statss.save()
    return redirect('/status')
@login_required
def editarStatus(request, id):
    stats= Status.objects.get(pk=id)
    return render(request,'adicionarStatus.html',context={'stats':stats})
@login_required
def excluirStatus(request,id):
    stats= Status.objects.get(pk=id)
    stats.delete()
    return redirect('/status')
@login_required
def listaCurso(request):
    cursos= Curso.objects.all()
    return render(request,'listaCurso.html',context={'cursos':cursos})
@login_required
def adicionarCurso(request):
    return render(request,'adicionarCurso.html',context=None)
@login_required
def salvarCurso(request):
    nome= request.POST.get('nome')
    id_curso= request.POST.get('id_curso')
    if id_curso:
        curso= Curso.objects.get(pk=id_curso)
    else:
        curso=Curso()

    curso.nome=nome
    curso.save()
    return redirect('/curso')
@login_required
def editarCurso(request,id):
    curso= Curso.objects.get(pk=id)
    return render(request,'adicionarCurso.html',context={'curso':curso})
@login_required
def excluirCurso(request,id):
    curso= Curso.objects.get(pk=id)
    curso.delete()
    return redirect('/curso')

@login_required
def listaDiasAtendimento(request):
    dias= DiasAtendimento.objects.all()
    return render(request,'listaDias.html',context={'dias':dias})
@login_required
def adicionarDias(request):
    return render(request, 'adicionarDias.html',context=None)
@login_required
def salvarDias(request):
    diaAtendimento= request.POST.get('dia_atendimento')
    horario_inicio= request.POST.get('horario_inicio')
    horario_termino= request.POST.get('horario_termino')
    id_dias= request.POST.get('id_dias')
    if id_dias:
        dias= DiasAtendimento.objects.get(pk=id_dias)
    else:
        dias= DiasAtendimento()

    dias.diaAtendimento=diaAtendimento
    dias.horario_inicio=horario_inicio
    dias.horario_termino=horario_termino
    dias.save()
    return redirect('/dias')
@login_required
def editarDias(request,id):
    dias= DiasAtendimento.objects.get(pk=id)
    return render(request,'adicionarDias.html',context={'dias':dias})
@login_required
def excluirDias(request,id):
    dias= DiasAtendimento.objects.get(pk=id)
    dias.delete()
    return redirect('/dias')

@login_required
def listaEstagiario(request):
    estagiarios= Estagiario.objects.all()
    return render(request,'listaEstagiario.html',context={'estagiarios':estagiarios})
@login_required
def adicionarEstagiario(request):
    diasAtendimento= DiasAtendimento.objects.all()
    return render(request,'adicionarEstagiario.html',context={'diasAtendimento':diasAtendimento})
@login_required
def editarEstagiario(request,id):
    estagiario= Estagiario.objects.get(pk=id)
    diasAtendimento= DiasAtendimento.objects.all()
    return render(request,'adicionarEstagiario.html',context={'estagiario':estagiario,'diasAtendimento':diasAtendimento})
@login_required
def excluirEstagiario(request,id):
    estagiario= Estagiario.objects.get(pk=id)
    estagiario.delete()
    return redirect('/estagiario')
@login_required
def salvarEstagiario(request):
    nome = request.POST.get('nome')
    cgu = request.POST.get('cgu')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    tipoEstagiario = request.POST.get('tipoEstagiario')
    diasAtendimento = request.POST.get('diasAtendimento')
    id_estagiario= request.POST.get('id_estagiario')
    if id_estagiario:
        estagiario= Estagiario.objects.get(pk=id_estagiario)
    else:
        estagiario=Estagiario()
    estagiario.nome=nome
    estagiario.cgu=cgu
    estagiario.cpf=cpf
    estagiario.telefone=telefone
    estagiario.tipoEstagiario=tipoEstagiario
    estagiario.diasAtendimento_id=diasAtendimento
    estagiario.save()
    return redirect('/estagiario')
@login_required
def listaRecurso(request):
    recursos= Recurso.objects.all()
    return render(request,'listaRecurso.html',context={'recursos':recursos})
@login_required
def adicionarRecurso(request):
    return render(request,'adicionarRecurso.html',context=None)
@login_required
def editarRecurso(request,id):
    recurso= Recurso.objects.get(pk=id)
    return render(request,'adicionarRecurso.html',context={'recurso':recurso})
@login_required
def excluirRecurso(request,id):
    recurso=Recurso.objects.get(pk=id)
    recurso.delete()
    return redirect('/recurso')

@login_required
def salvarRecurso(request):
    nome= request.POST.get('nome')
    descricao= request.POST.get('descricao')
    quantidade= request.POST.get('quantidade')
    id_recurso= request.POST.get('id_recurso')
    if id_recurso:
        recurso= Recurso.objects.get(pk=id_recurso)
    else:
        recurso= Recurso()

    recurso.nome=nome
    recurso.descricao=descricao
    recurso.quantidade=quantidade
    recurso.save()
    return redirect('/recurso')