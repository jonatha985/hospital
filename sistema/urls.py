from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre_nos/', views.sobre, name='sobre'),
    path('admin/login_admin/', views.login_admin, name='login_admin'),
    path('equipe/login_doctor/', views.login_doctor, name='login_doctor'),
    path('recepionista/login_recep/', views.login_recep, name='login_recep'),
    path('admin/dashboard/', views.dash_admin, name='dash_admin'),
    path('doctor/dashboard/', views.dash_doctor, name='dash_doctor'),
    path('recepcionista/dashboard/', views.dash_recep, name='dash_recep'),
    path('add/recepcionista/', views.add_recepcionista, name='add_recepcionista'),
    path('add/profissional/', views.add_doctor, name='add_doctor'),
    path('lista/profissionais/', views.listar_profissionais, name='listar_profissionais'),
    path('atender_paciente/', views.atender_paciente, name='atender_paciente'),
    path('Logout/', views.sair, name="sair"),
]
