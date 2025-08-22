from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from . import models
from django.urls import reverse, reverse_lazy
from . import forms
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, SingleTableView, RequestConfig
from . import tables
from . import filters

class roster_home(TemplateView):
    template_name = "person_base.html"
    #return render(request, "roster_base.html", context={})

def load_people(request):
    model = get_user_model()
    context = {}
    table = tables.PeopleListTable(model.objects.order_by('last_name').exclude(username='admin'))
    #RequestConfig(request, paginate={"per_page": "10" }).configure(table)
    context['table'] = table
    return render(request, 'Roster/person_list_part.html', context)

class CreatePerson(SingleTableMixin, CreateView):
    model = get_user_model()
    template_name = "Roster/person_form.html"
    form_class = forms.PersonForm
    success_url = reverse_lazy('roster-home')

class UpdatePerson(UpdateView):
    model = get_user_model()
    template_name = "Roster/person_form.html"
    form_class = forms.PersonForm
    success_url = reverse_lazy('roster-home')
class DeletePerson(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('roster-home')

class PersonView(SingleTableView):
    Person = get_user_model()
    model = Person
    form_class = forms.PersonForm
    #fields = ['first_name', 'last_name', 'username', 'email', 'affiliation' ]
    queryset = Person.objects.order_by('last_name').exclude(username='admin')
    context_object_name = 'people'
    table_class = tables.PeopleListTable
    #filterset_class = filters.PersonFilter
    table_pagination = {
        "per_page": 10,
    }

class UpdateTemplate(TemplateView):
    template_name = "Roster/person_form.html"
