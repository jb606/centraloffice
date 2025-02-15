from django.db import models
from django.contrib.auth import get_user_model
BOOTSTRAP_BUTTON_CHOICES = (
   ( "btn-primary", "Primary"),
   ( "btn-secondary", "Secondary"),
   ( "btn-success", "Success"),
   ( "btn-danger", "Danger"),
   ( "btn-warning", "Warning"),
   ( "btn-info", "Infomation"),
   ( "btn-light", "Light"),
   ( "btn-dark", "Dark"),
   ( "btn-link", "Link"),
)

Person = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=50)
    css = models.CharField(max_length=15,
                  choices=BOOTSTRAP_BUTTON_CHOICES,
                  )
    class Meta:
        verbose_name_plural = "Status"
        verbose_name = "Status"
        db_table = "status"
    def __str__(self):
        return f"{self.name}"

class PersonStatus(models.Model):
    class Meta:
        verbose_name_plural = "PersonStatus"
        verbose_name = "PersonStatus"
        db_table = "person_status"
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="status")
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    nightly_reset = models.BooleanField(default=False)
    notes = models.CharField(max_length=100)
class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    members = models.ManyToManyField(PersonStatus, related_name="member_of")
    mods = models.ManyToManyField(PersonStatus, related_name="moderating")
