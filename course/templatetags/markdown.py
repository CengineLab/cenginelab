from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown as md

from markdown.extensions.codehilite import CodeHilite, CodeHiliteExtension

register = template.Library()


@register.filter(name="markdown")
@stringfilter
def markdown(value):
    generated_html = md.markdown(value, extensions=['fenced_code', CodeHiliteExtension(pygments_style='native', linenos=False), 'extra', "footnotes"])
    return mark_safe(f"<div class='markdown'>{generated_html}</div>")