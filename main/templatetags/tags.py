from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    return 'active-page' if pattern == request.path else ''
