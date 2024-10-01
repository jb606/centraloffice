from django.contrib import admin
from .models import Person, Affiliation, Citizenship, EmergencyContact
# Register your models here.

admin.site.register(Person)
admin.site.register(Affiliation)
admin.site.register(Citizenship)
admin.site.register(EmergencyContact)