from django.shortcuts import render

# Create your views here.
def inicio(request): #direciona para o link da página inicial do projeto
    return render(request, 'inicio/index.html') #endereço da página inicial renderiza e para a página inicial padrão
