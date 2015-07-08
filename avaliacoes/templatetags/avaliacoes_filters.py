
# -*- coding: utf-8 -*-
from django import template


register = template.Library()

@register.filter(name='teste')
def teste(model, field):
    if hasattr(model, field):
        return getattr(model, field)
    else:
        return None