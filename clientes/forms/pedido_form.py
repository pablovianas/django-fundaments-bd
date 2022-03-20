from django import forms
from ..models import Pedido, Cliente, Produto

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all()) #busca todos os clientes do bd
    produtos = forms.ModelMultipleChoiceField(queryset=Produto.objects.all()) #busca todos os clientes do bd
    class Meta:
        model = Pedido
        fields = ['cliente', 'data_pedido', 'produtos', 'valor', 'status', 'observacoes']