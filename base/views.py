from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Q

from.forms import Form

from .models import *
from .carrinho import Carrinho

def base(request):
    produtos = Produto.objects.all()[0:8]
    return render(request, "base/base.html", {'produtos':produtos})

def signup(request):
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            usuario = form.save()

            login(request, usuario)

            return redirect('/login/')
    else:
        form = Form()

    return render(request, 'base/signup.html', {
        'form': form
    })

def products(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all() 

    active_categoria = request.GET.get('categoria', '')

    if active_categoria:
        produtos = produtos.filter(categoria__slug=active_categoria)

    query = request.GET.get('query', '')

    if query:
        produtos = produtos.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))

    contexto = {
        'categorias': categorias,
        'produtos': produtos,
        'active_categoria': active_categoria
    }

    return render(request, 'products/products.html', contexto)

def product(request, slug):
    produto = get_object_or_404(Produto, slug=slug)

    return render(request, 'products/product.html', {'produto':produto})

def add_cart(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.add(produto_id)
    
    return render(request, 'cart/add_cart.html', {'carrinho': carrinho})

def cart(request):
    return render(request, 'cart/cart.html')

def custom_logout(request):
    logout(request)

    return redirect('/')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')