"""apiAlteridade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alteridade.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',do_logout,name='logout'),
    path('index/',index,name='index'),
    path('autenticar/',do_login,name='login'),

    path('status/',listaStatus,name='lista_status'),
    path('status/add',adicionarStatus,name='adicionar_status'),
    path('status/salvar',salvarStatus,name='salvar_status'),
    path('status/editar/<int:id>/',editarStatus,name='editar_status'),
    path('status/excluir/<int:id>/',excluirStatus,name='excluir_status'),

    path('curso/',listaCurso,name='lista_curso'),
    path('curso/add',adicionarCurso,name='adicionar_curso'),
    path('curso/salvar',salvarCurso,name='salvar_curso'),
    path('curso/editar/<int:id>/',editarCurso,name='editar_curso'),
    path('curso/excluir/<int:id>/',excluirCurso,name='excluir_curso'),

    path('dias/',listaDiasAtendimento,name='lista_dias'),
    path('dias/add',adicionarDias,name='adicionar_dias'),
    path('dias/salvar',salvarDias,name='salvar_dias'),
    path('dias/editar/<int:id>/',editarDias,name='editar_dias'),
    path('dias/excluir/<int:id>/',excluirDias,name='excluir_dias'),

    path('estagiario/',listaEstagiario,name='lista_estagiario'),
    path('estagiario/add',adicionarEstagiario,name='adicionar_estagiario'),
    path('estagiario/salvar',salvarEstagiario,name='salvar_estagiario'),
    path('estagiario/editar/<int:id>/',editarEstagiario,name='editar_estagiario'),
    path('estagiario/excluir/<int:id>/',excluirEstagiario,name='excluir_estagiario'),

    path('recurso/',listaRecurso,name='lista_recurso'),
    path('recurso/add',adicionarRecurso,name='adicionar_recurso'),
    path('recurso/salvar',salvarRecurso,name='salvar_recurso'),
    path('recurso/editar/<int:id>/',editarRecurso,name='editar_recurso'),
    path('recurso/excluir/<int:id>/',excluirRecurso,name='excluir_recurso'),

    path('categoria/',listaCategoria,name='lista_categoria'),
    path('categoria/add',adicionarCategoria,name='adicionar_categoria'),
    path('categoria/salvar',salvarCategoria,name='salvar_categoria'),
    path('categoria/editar/<int:id>/',editarCategoria,name='editar_categoria'),
    path('categoria/excluir/<int:id>/',excluirCategoria,name='excluir_categoria'),   

]
