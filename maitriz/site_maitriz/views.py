from django.shortcuts import render, get_object_or_404
from .models import Conteudo, Menu

def obter_menu():
    return Menu.objects.filter(ativo=True).order_by('ordem')

def home(request):
    return render(request, 'site_maitriz/home.html', {'menu': obter_menu()})

def conteudo(request, slug):
    pagina = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'site_maitriz/conteudo.html', {
        'menu': obter_menu(),
        'conteudo': pagina,
    })