from django.urls import path

from django.contrib.auth import views 

from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
    path('login/', views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('products/', products, name='products'),
    path('product/<slug:slug>/', product, name='product'),
    path('carrinho-compras/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu_carrinho/<int:produto_id>/', add_cart, name='add_cart'),
]