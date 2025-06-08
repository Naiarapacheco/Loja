from .carrinho import Carrinho

#available everywhere
def carrinho(request):
    return {'carrinho': Carrinho(request)}