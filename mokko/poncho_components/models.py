from django.db import models

# Create your models here.
# TODO models for ponchocomponents
class PonchoComponents(models.Model):
    componentname = models.CharField(max_length=200)

class PonchoProps(models.Model):
    propname = models.CharField(max_length=100)
    proptype = models.CharField(max_length=200)