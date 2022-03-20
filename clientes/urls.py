from unicodedata import name
from django.urls import path
from clientes.services.cliente_service import cadastrar_cliente

from clientes.services.pedido_service import listar_pedido_id
from .views.cliente_views import *
from .views.pedido_views import *
from .views.produto_views import *

urlpatterns =[
    path('listar_clientes', listar_clientes, name='listar_clientes'),
    path('cadastrar_clientes', inserir_cliente, name='cadastrar_cliente'),
    path('listar_cliente/<int:id>', listar_cliente_id, name = 'listar_cliente_id'),
    path('editar_cliente/<int:id>', editar_cliente, name ='editar_cliente'),
    path('remover_cliente/<int:id>', remover_cliente, name='remover_cliente'),
    path('cadastrar_pedido', inserir_pedido, name='cadastrar_pedido'),
    path('listar_pedidos', listar_pedidos, name="listar_pedido" ),
    path('listar_pedido/<int:id>', listar_pedidos_id, name = 'listar_pedido_id'),
    path('editar_pedido/<int:id>', editar_pedidos, name ='editar_pedidos'),
    path('cadastrar_produtos', inserir_produto, name="inserir_produto"),
    path('listar_produtos', listar_produtos, name="listar_produtos" ),
    path('listar_produto/<int:id>', listar_produtos_id, name = 'listar_produtos_id'),
    

]