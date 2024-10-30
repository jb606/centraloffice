from django.contrib import admin
from . import models

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',  )

admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Affiliation)