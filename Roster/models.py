from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.text import slugify

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
    slug = models.SlugField(unique=True, blank=True)
    def __str__ (self):
        return(f"{self.first_name} {self.last_name}")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "People"
        verbose_name = "Person"
        db_table = "people"
