from django.contrib.auth import get_user_model
from django_tables2.views import SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from django.shortcuts import render

from . import tables, forms, filters, models

# Create your views here.
def sb_home(request):
    return render(request, "sb_base.html", context={})

class GroupListView(SingleTableMixin, FilterView):
    model = models.Group
    template_name = "StatusBoard/sb_filter.html"
    table_class = tables.GroupTable
    filterset_class = filters.GroupFilter
    table_pagination = {
        "per_page": 25,
    }

class GroupView(SingleTableMixin, DetailView):
    model = models.Group
    template_name = "StatusBoard/sb_form.html"
    table_class = tables.GroupTable

class GroupCreate(CreateView):
    model = models.Group
    success_url = reverse_lazy("sb-default")
    form_class = forms.GroupForm
    template_name = "StatusBoard/sb_form.html"