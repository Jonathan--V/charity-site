import re
from django import template

from main.constants import all_constants

register = template.Library()


@register.simple_tag
def active(request, pattern):
    return 'active-page' if pattern == request.path else ''


@register.simple_tag
def constant(name):
    return all_constants[name]
