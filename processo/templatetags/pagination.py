# coding=utf-8
"""
    É uma função generica que executa uma paginação otimizada já integrada com o ORM do django
    e integrada com class-based-view, só requisitando a quantidade de objetos que forem
    inseridos no atributo paginate_by.
    A função urlencode insere todas as variaveis na url do browser já inserindo o separador '&'
"""

from django.template import Library

register = Library()


@register.inclusion_tag('processo/pagination.html')
def pagination(request, paginator, page_obj):
    """
        É uma função generica que executa uma paginação otimizada já integrada com o ORM do django
        e integrada com class-based-view, só requisitando a quantidade de objetos que forem
        inseridos no atributo paginate_by.
        A função urlencode insere todas as variaveis na url do browser já inserindo o separador '&'
    """
    context = {}
    context['paginator'] = paginator
    context['request'] = request
    context['page_obj'] = page_obj
    getvars = request.GET.copy()
    if 'page' in getvars:
        del getvars['page']
    if len(getvars) > 0:
        context['getvars'] = '&{0}'.format(getvars.urlencode())
    else:
        context['getvars'] = ''
    return context
