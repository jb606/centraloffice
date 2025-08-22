from django import template
from django.utils.html import format_html
register = template.Library()

@register.simple_tag
def load_menu():
    pass