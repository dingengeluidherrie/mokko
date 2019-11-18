from django.db import models

# Create your models here.
# TODO models for ponchocomponents
class PonchoComponents(models.Model):
    componentname = models.CharField(max_length=200)

# class OptioneleProducten(models.Model):
#     productcode = models.CharField(max_length=2)