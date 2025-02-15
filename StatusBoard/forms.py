from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,HTML, Layout, Row, Column
from crispy_forms.bootstrap import FormActions
from . import models


class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = [ 'name', 'description' ]
    layout = Layout(
        'name',
        'description',
        FormActions(
            Submit('submit', 'Submit', css_class='btn btn-sm'),
            #HTML('<a href="{% url "sb-default" %}" class="btn btn-sm btn-link">Cancel</a>'),
        )
    )
    helper = FormHelper()
    helper.layout = layout
