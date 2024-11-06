from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from . import models
from django.urls import reverse, reverse_lazy
from . import forms
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from . import tables
from . import filters

def roster_home(request):
    return render(request, "roster_base.html", context={})

class CreatePerson(SingleTableMixin, CreateView):
    model = get_user_model()
    template_name = "Roster/person_form.html"
    form_class = forms.PersonForm
    success_url = reverse_lazy('person-list')

class UpdatePerson(UpdateView):
    model = get_user_model()
    template_name = "Roster/person_form.html"
    form_class = forms.PersonForm
    success_url = reverse_lazy('person-list')
class DeletePerson(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('person-list')

class PersonView(SingleTableMixin, FilterView):
    Person = get_user_model()
    model = Person
    form_class = forms.PersonForm
    #fields = ['first_name', 'last_name', 'username', 'email', 'affiliation' ]
    queryset = Person.objects.order_by('last_name').exclude(username='admin')
    context_object_name = 'people'
    table_class = tables.PeopleListTable
    filterset_class = filters.PersonFilter
    table_pagination = {
        "per_page": 25,
    }

class UpdateTemplate(TemplateView):
    template_name = "Roster/person_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = get_object_or_404(get_user_model(),pk=self.kwargs['pk'])
        context['person'] = person
        context['form'] = forms.PersonForm(instance=person)
        context['profile_form'] = forms.ProfileForm(instance=person.profile)
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        person = get_object_or_404(get_user_model(), pk=pk)
        person_form = forms.PersonForm(instance=person)
        profile = get_object_or_404(models.Profile, person__pk=pk)
        profile_form = forms.ProfileForm(instance=profile, data=request.POST)
        if 'save_person' in request.POST:
            if person_form.is_bound and person_form.is_valid():
                person_form.save()