from django import forms
from .models import Person, Affiliation

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'personal_email': 'Personal Email',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zipcode',
            'affiliation': 'Affiliation',
            'citizenship': 'Citizenship',
            'emergencycontact': 'Emergency Contacts',

        }
    
class AffilationForm(forms.ModelForm):
    class Meta:
        model = Affiliation
        fields = '__all__'

    labels = {
        'name': 'Name',
        'abbreviation': 'Abbreviation',
        'description': 'Description',
    }
    widgets = {
        'name': forms.TextInput(),
        'abbreviation': forms.TextInput(),
        'description': forms.TextInput(),
    }

