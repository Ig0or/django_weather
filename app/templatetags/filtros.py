from django import template

register = template.Library()

@register.filter(name='converter')
def converter(value):
    return round(value - 273)