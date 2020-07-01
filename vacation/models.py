from django.db import models
from django.conf import settings

# Create your models here.
class Vacation(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=200)
    datetime_from = models.DateField()
    datetime_to = models.DateField()