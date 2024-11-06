from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class Affiliation(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.CharField(max_length=50, blank=True)
    def __str__ (self):
        return(f"{self.abbreviation}")

class Person(AbstractUser):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True, null=False)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE, blank=True, null=True)
    email = models.CharField(max_length=50,
                             blank=False,
                             help_text="Required",
                             error_messages={
                                 'unique': 'A user with that email address already exists',
                                             }
                            )
    def __str__ (self):
        return(f"{self.first_name} {self.last_name}")
    class Meta:
        verbose_name_plural = "People"
        verbose_name = "Person"
        db_table = "people"

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    home_phone = models.CharField(max_length=16, null=True, blank=True)
    mobile_phone = models.CharField(max_length=16, null=True, blank=True)
    def __str__(self):
        return self.user.username
