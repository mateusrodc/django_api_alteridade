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

    path('servico/',listaServico,name='lista_servico'),
    path('servico/add',adicionarServico,name='adicionar_servico'),
    path('servico/salvar',salvarServico,name='salvar_servico'),
    path('servico/editar/<int:id>/',editarServico,name='editar_servico'),
    path('servico/excluir/<int:id>/',excluirServico,name='excluir_servico'),

    path('deficiencia/',listaDeficiencia,name='lista_deficiencia'),
    path('deficiencia/add',adicionarDeficiencia,name='adicionar_deficiencia'),
    path('deficiencia/salvar',salvarDeficiencia,name='salvar_deficiencia'),
    path('deficiencia/editar/<int:id>/',editarDeficiencia,name='editar_deficiencia'),
    path('deficiencia/excluir/<int:id>/',excluirDeficiencia,name='excluir_deficiencia'),

    path('academico/',listaAcademico,name='lista_academico'),
    path('academico/add',adicionarAcademico,name='adicionar_academico'),
    path('academico/salvar',salvarAcademico,name='salvar_academico'),
    path('academico/editar/<int:id>/',editarAcademico,name='editar_academico'),
    path('academico/excluir/<int:id>/',excluirAcademico,name='excluir_deficiencia'),

    path('agendamento/',listaAgendamento,name='lista_agendamento'),
    path('agendamento/add',adicionarAgendamento,name='adicionar_agendamento'),
    path('agendamento/salvar',salvarAgendamento,name='salvar_agendamento'),
    path('agendamento/editar/<int:id>/',editarAgendamento,name='editar_agendamento'),
    path('agendamento/excluir/<int:id>/',excluirAgendamento,name='excluir_agendamento'),
    

]
