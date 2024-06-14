from django import template

register = template.Library()


@register.filter
def reverse(item):
    return item[::-1]
