
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html



register = template.Library()


@register.simple_tag(name='svg_icon')
def svg_icon(svg_html, extra_class=''):
     svg_tag = svg_html
    
     return mark_safe(svg_tag)