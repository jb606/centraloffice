from django import template
from django.utils.html import format_html
register = template.Library()

@register.simple_tag
def status_modal_target():
    html = """
<div id="set_status" class="modal fade" role="dialog">
   <div id="set_status_dialog" class="modal-dialog" role="document" hx-target="modal-dialog"></div>
</div>
"""
    return format_html(html)