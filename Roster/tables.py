from django_tables2 import tables, TemplateColumn
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PeopleListTable(tables.Table):
    class Meta:
        model = User
        attrs = {'class': 'table table-sm'}
        fields = [
            "last_name",
            "first_name",
            "email",
            "affiliation__name",
            "actions",
        ]
    
    actions = TemplateColumn(template_name="Roster/list_actions.html")
    affiliation__name = tables.Column(verbose_name="Affiliation")
    def before_render(self, request):
        if request.user.is_staff:
            self.columns.show('actions')
        else:
            self.columns.hide('actions')