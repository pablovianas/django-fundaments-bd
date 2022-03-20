from django import template

register = template.Library() #registra uma novo filtro 

@register.filter(name='addclass')

def addClass(value, arg):
    return value.as_widget(attrs={'class':arg})