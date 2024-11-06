from django_filters import FilterSet
from django.contrib.auth import get_user_model

User = get_user_model()

class PersonFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            "last_name": ["contains"],
            "first_name": [ "contains"],
            "username": ['contains'],
                  }