from django.shortcuts import redirect, render
from ..entidades import pedido
from ..forms import pedido_form
from ..services import pedido_service, produto_service


def inserir_pedido(request):
    if request.method == 'POST':
        form_pedido = pedido_form.PedidoForm(request.POST)
        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data['cliente']
            data_pedido = form_pedido.cleaned_data['data_pedido']
            valor = form_pedido.cleaned_data['valor']
            status = form_pedido.cleaned_data['status']
            observacoes = form_pedido.cleaned_data['observacoes']
            produtos = form_pedido.cleaned_data['produtos']

            pedido_novo = pedido.Pedido(cliente=cliente, data_pedido=data_pedido, valor=valor, status=status, observacoes=observacoes, produtos=produtos)

            pedido_service.cadastrar_pedido(pedido_novo)
            return redirect('listar_pedido')
    else:
        form_pedido = pedido_form.PedidoForm()
    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})

def listar_pedidos(request):
    pedidos = pedido_service.listar_pedidos()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

def listar_pedidos_id(request, id):
    pedido = pedido_service.listar_pedido_id(id)

    
    return render(request, 'pedidos/lista_pedido.html', {'pedido':pedido})

def editar_pedidos(request, id):
    pedido_antigo = pedido_service.listar_pedido_id(id)
    form_pedido = pedido_form.PedidoForm(request.POST or None, instance=pedido_antigo)

    if form_pedido.is_valid():
        cliente = form_pedido.cleaned_data['cliente']
        data_pedido = form_pedido.cleaned_data['data_pedido']
        valor = form_pedido.cleaned_data['valor']
        status = form_pedido.cleaned_data['status']
        observacoes = form_pedido.cleaned_data['observacoes']
        produtos = form_pedido.cleaned_data['produtos']


        pedido_novo = pedido.Pedido(cliente=cliente, data_pedido=data_pedido, valor=valor, status=status, observacoes=observacoes, produtos=produtos)

        pedido_service.editar_pedido(pedido_antigo, pedido_novo)
        return redirect('listar_pedido')
    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})
