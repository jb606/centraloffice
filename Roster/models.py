from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
from django_countries.fields import CountryField

# Create your models here.



class Affiliation(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.CharField(max_length=50, blank=True)
    def __str__ (self):
        return(f"{self.abbreviation}")

class Citizenship(models.Model):
    name = CountryField()
    description = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return(f"{self.name.code}")

class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    relationship = models.CharField(max_length=50)
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class Person(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    personal_email = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=16, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = USStateField(blank=True)
    zipcode = USZipCodeField(blank=True)
    country = CountryField(blank=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.SET_NULL, null=True, blank=True)
    citizenship = models.ManyToManyField(Citizenship, blank=True, related_name='person')
    emergencycontact = models.ManyToManyField(EmergencyContact, blank=True, related_name='person')



    def __str__ (self):
        return(f"{self.first_name} {self.last_name}")

    class Meta:
        verbose_name_plural = "People"
        verbose_name = "Person"
        db_table = "people"
