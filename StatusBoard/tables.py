from django_tables2 import tables, TemplateColumn, LinkColumn
from . import models
from django.contrib.auth import get_user_model
from django_tables2.utils import A
Person = get_user_model()

class GroupTable(tables.Table):
    name = LinkColumn("sb-group-view", args=[A("pk")])
    class Meta:
        model = models.Group
        attrs = {'class': 'table table-sm'}
        fields = [ 'name', 'description']
    #actions = TemplateColumn(template_name="Roster/list_actions.html")