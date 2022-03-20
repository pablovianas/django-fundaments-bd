from ..models import Pedido
from ..services import produto_service

def cadastrar_pedido(pedido):
    pedido_bd = Pedido.objects.create(cliente= pedido.cliente, data_pedido = pedido.data_pedido, valor=pedido.valor, status = pedido.status, observacoes=pedido.observacoes)
    pedido_bd.save()

    for i in pedido.produtos:
        produto = produto_service.listar_produtos_id(i.id)
        pedido_bd.produtos.add(produto)
        
def listar_pedidos():
    pedidos = Pedido.objects.select_related('cliente').all() #só funciona em relacionamento 1:1 ou 1:N todos de todos 
    return pedidos

def editar_pedido(pedido, pedido_novo):
    pedido.cliente = pedido_novo.cliente
    pedido.data_pedido = pedido_novo.data_pedido
    pedido.valor = pedido_novo.valor
    pedido.status = pedido_novo.status
    pedido.observacoes = pedido_novo.observacoes
    pedido.produtos.set(pedido_novo.produtos)
    pedido.save(force_update=True)

def listar_pedido_id(id):
    pedido = Pedido.objects.get(id=id) 
    return pedido

def remover_pedido(pedido):
    pedido.delete()