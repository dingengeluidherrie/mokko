from django.db import models

# Create your models here.

class Lidmaatschapsproducten(models.Model):
    productnaam = models.CharField(max_length=200)
    productcode = models.CharField(max_length=200)
    graad = models.CharField(max_length=200)
    dekking = models.CharField(max_length=200)

class OptioneleProducten(models.Model):
    productcode = models.ArrayField()

class Geslachten(models.Model):
    geslacht = models.CharField(max_length=10)

class Betaaltermijnen(models.Model):
    termijn = models.CharField(max_length=10)

class Productovereenkomsten(models.Model):
    overeenkomst = models.CharField(max_length=10)

class Kanaalspecificatiecodes(models.Model):
    spec = models.IntegerField()

class Businessprocessen(models.Model):
    proces = models.CharField(max_length=50)

class Afspraken(models.Model):
    afspraak = models.CharField(max_length=50)