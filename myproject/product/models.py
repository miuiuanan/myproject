from django.db import models


# Create your models here.
class category(models.Model):
    id=models.IntegerField("Id",primary_key=True)
    name=models.CharField("Name",max_length=256)
