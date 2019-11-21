from django.db import models
from django.contrib.auth.models import Group
# Create your models here.

class Lidmaatschapsproducten(models.Model):
    productnaam = models.CharField(max_length=200)
    productcode = models.CharField(max_length=200)
    graad = models.CharField(max_length=200)
    dekking = models.CharField(max_length=200)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.productnaam

class OptioneleProducten(models.Model):
    productcode = models.CharField(max_length=2)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.productcode

class Geslachten(models.Model):
    geslacht = models.CharField(max_length=10)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.geslacht

class Betaaltermijnen(models.Model):
    termijn = models.CharField(max_length=10)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.termijn

class Productovereenkomsten(models.Model):
    overeenkomst = models.CharField(max_length=10)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.overeenkomst

class Kanaalspecificatiecodes(models.Model):
    spec = models.IntegerField()
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.spec

class Businessprocessen(models.Model):
    proces = models.CharField(max_length=50)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.proces

class Afspraken(models.Model):
    afspraak = models.CharField(max_length=50)
    user_group = models.ManyToManyField(Group)

    def __str__(self):
        return self.afspraak