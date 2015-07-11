
# -*- coding: utf-8 -*-
from django import template


register = template.Library()

@register.filter(name='field')
def field(model, field):
    if hasattr(model, field):
        return getattr(model, field)
    else:
        return None


@register.filter(name='field_parq')
def field_parq(model, field):
    if hasattr(model, field):
        if getattr(model, field) == True:
            return "Sim"
        elif getattr(model, field) == False:
            return "Não"
        else:
            return "Desconhecido"
    else:
        return None