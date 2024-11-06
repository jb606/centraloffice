from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,HTML, Layout, Row, Column
from crispy_forms.bootstrap import FormActions
from . import models
class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = "__all__"
        exclude = ['user']

    helper = FormHelper()
    helper.layout = Layout(
            Row(
                Column('home_phone'),
                Column('mobile_phone'),
            ),
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-sm'),
                HTML('<a href="{% url "person-list" %}" class="btn btn-sm btn-link">Cancel</a>'),
          )

        )

class PersonForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "affiliation",
            "username",
        ]

    layout = Layout(
        Row(
            Column('first_name'),
            Column('middle_name'),
            Column('last_name'),
        ),
        Row(
            Column('username', css_class="col-sm-3"),
            Column('email'),
        ),
        Row(
            Column('affiliation'),
        ),
        FormActions(
            Submit('submit', 'Submit', css_class='btn btn-sm'),
            HTML('<a href="{% url "person-list" %}" class="btn btn-sm btn-link">Cancel</a>'),
        )
    )
    helper = FormHelper()
    helper.layout = layout