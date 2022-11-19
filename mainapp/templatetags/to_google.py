from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def redirect_to_google(value):
    return mark_safe(f"<a  href='https://www.google.com/search?q={value}'>{value}</a>")
