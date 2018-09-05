from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Importa formulários
from sistema.forms import LinhasForm, CategoriasForm, ProdutosForm
# Importa modelos
from sistema.models import Linhas, Categorias, Produtos

# Create your views here.

def index(request):
    return render(request, "website/index.html")

# --- CRUD LINHAS ---
def cadastrar_linhas(request):
    
    if request.method == 'POST':
        form = LinhasForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('website:consultar_linhas')
        else:
            print(form.errors)
    else:
        form = LinhasForm()
    return render(request, "website/cadastrar_linhas.html", {'form': form})

def consultar_linhas(request):
    linhas_lista = Linhas.objects.all()
    contexto = {'linhas': linhas_lista}
    return render(request, "website/consultar_linhas.html", contexto)

def deletar_linhas(request, id):
    linha = Linhas.objects.get(id=id).delete()
    return redirect('website:consultar_linhas')

def editar_linhas(request, id):
    linha = get_object_or_404(Linhas, id=id)
    form = LinhasForm(request.POST or None, instance=linha)

    if form.is_valid():
        form.save()
        return redirect('website:consultar_linhas')

    return render(request, 'website/cadastrar_linhas.html', {"form":form})
# --- CRUD CATEGORIAS ---
def cadastrar_categorias(request):
    
    if request.method == 'POST':
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:consultar_categorias')
        else:
            print(form.errors)
    else:
        form = CategoriasForm()
    return render(request, "website/cadastrar_categorias.html", {'form': form})

def consultar_categorias(request):
    categorias_lista = Categorias.objects.all()
    contexto = {'categorias': categorias_lista}
    return render(request, "website/consultar_categorias.html", contexto)

def deletar_categorias(request, id):
    categoria = Categorias.objects.get(id=id).delete()
    return redirect('website:consultar_categorias')

def editar_categorias(request, id):
    categoria = get_object_or_404(Categorias, id=id)
    form = CategoriasForm(request.POST or None, instance=categoria)
    
    if form.is_valid():
        form.save()
        return redirect('website:consultar_categorias')

    return render(request, 'website/cadastrar_categorias.html', {"form":form})

# --- CRUD PRODUTOS ---

def cadastrar_produtos(request):
    
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:consultar_produtos')
        else:
            print(form.errors)
    else:
        form = ProdutosForm()
    return render(request, "website/cadastrar_produtos.html", {'form': form})

def consultar_produtos(request):
    produtos_lista = Produtos.objects.all()
    contexto = {'produtos': produtos_lista}
    return render(request, "website/consultar_produtos.html", contexto)

def deletar_produtos(request, id):
    produto = Produtos.objects.get(id=id).delete()
    return redirect('website:consultar_produtos')

def editar_produtos(request, id):
    produto = get_object_or_404(Produtos, id=id)
    form = ProdutosForm(request.POST or None, instance=produto)
    
    if form.is_valid():
        form.save()
        return redirect('website:consultar_produtos')
    
    return render(request, 'website/cadastrar_produtos.html', {"form":form})

