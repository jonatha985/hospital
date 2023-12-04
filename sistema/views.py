from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .decorators import recepcionista, doutor
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
# Create your views here.

def index(request):
    return render(request, 'sistema/index.html')


def sobre(request):
    return render(request, 'sistema/sobre.html')


def login_admin(request):
    if request.method == "GET":
        return render(request, 'sistema/login_admin.html')
    else:
        nome = request.POST.get("nome").strip()
        senha = request.POST.get("senha")
        usuario_admin = authenticate(username=nome, password=senha)
        if usuario_admin:
            login(request, usuario_admin)
            return redirect('dash_admin')
        else:
            messages.error(request, 'Usuario ou senha inválidos !')
            return redirect('login_admin')

def login_doctor(request):
    if request.method == "GET":
        return render(request, 'sistema/login_doctor.html')
    else:
        nome = request.POST.get("nome").strip()
        senha = request.POST.get("senha")
        usuario_doctor = authenticate(username=nome, password=senha)
        if usuario_doctor:
            login(request, usuario_doctor)
            return redirect('dash_doctor')
        else:
            messages.error(request, 'Usuario ou senha inválidos !')
            return redirect('login_doctor')

def login_recep(request):
    if request.method == "GET":
        return render(request, 'sistema/login_recep.html')
    else:
        nome = request.POST.get("nome").strip()
        senha = request.POST.get("senha")
        usuario_recep = authenticate(username=nome, password=senha)
        if usuario_recep:
            login(request, usuario_recep)
            return redirect('dash_recep')
        else:
            messages.error(request, "Usuario ou senha invalidos !")
            return redirect('login_recep')

@login_required
def dash_admin(request):
    return render(request, 'sistema/dash_admin.html')

@login_required
def dash_doctor(request):
    return render(request, 'sistema/dash_doctor.html')

@login_required
def dash_recep(request):
    return render(request, 'sistema/dash_recep.html')

@login_required
def sair(request):
    if not request.user.is_staff:
        return redirect('index')
    logout(request)
    return redirect('index')

@login_required
def add_recepcionista(request):
    return render(request, "sistema/add_recepcionista.html")


@login_required
def add_doctor(request):
    if request.method == "GET":
        return render(request, 'sistema/add_doctor.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        crm = request.POST.get("crm")
        email = request.POST.get("email")
        especialidade = request.POST.get("especialidade")
        if User.objects.filter(username=username).exists():
            messages.error(request,"Usuario ja existe !")
            return redirect('add_doctor')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.set_password(password)
            user.save()
            assign_role(user, 'doutor')
            print("Salvo com sucesso")
            return redirect('add_doctor')
    return render(request, "sistema/add_doctor.html")


@login_required
def listar_profissionais(request):
    return render(request, "sistema/listar_profissionais.html")

@login_required
def atender_paciente(request):
    return render(request,"sistema/atender_paciente.html")