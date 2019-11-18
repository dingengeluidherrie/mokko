from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import (
    Lidmaatschapsproducten,
    OptioneleProducten,
    Afspraken,
    Kanaalspecificatiecodes,
    Betaaltermijnen,
    Businessprocessen,
    Geslachten,
    Productovereenkomsten,
)
from .utils import combs, model_to_dict_remove_id
from faker import Faker
import random
from itertools import combinations
import json

# Create your views here.
fake = Faker("nl_NL")


@csrf_exempt
def dingen(request):

    json_body = json.loads(request.body)
    response = json_body

    # TODO: extract a method to check the json_body keys as local variables. Cleaner code :)
    if "lidmaatschapsproduct" not in json_body:
        response["lidmaatschapsproduct"] = model_to_dict_remove_id(
            Lidmaatschapsproducten.objects.order_by("?").first()
        )
    if "afspraken" not in json_body:
         afspraken = list(Afspraken.objects.all())
         afspraken = [None] + [model_to_dict_remove_id(x) for x in afspraken]
         choice = random.choice(afspraken)
         if choice is not None:
            response["afspraken"] = choice
    if "businessproces" not in json_body:
        response["businessproces"] = model_to_dict_remove_id(
            Businessprocessen.objects.order_by("?").first()
        )
    if "kanaalspecificatiecode" not in json_body:
        response["kanaalspecificatiecode"] = model_to_dict_remove_id(
            Kanaalspecificatiecodes.objects.order_by("?").first()
        )
        # TODO: if both birthdate and productovereenkomst are proviced, use given data.
        # (they are interdependent, but if the user wants conflicting data they can have it >:D )
    if "productovereenkomst" not in json_body:
        response["productovereenkomst"] = model_to_dict_remove_id(
            Productovereenkomsten.objects.order_by("?").first()
        )    
    if "betaaltermijn" not in json_body:
        response["betaaltermijn"] = model_to_dict_remove_id(
            Betaaltermijnen.objects.order_by("?").first()
        )    
    if "gender" not in json_body:
        response["gender"] = model_to_dict_remove_id(
            Geslachten.objects.order_by("?").first()
        )                  
        # TODO: Make optioneleproduct dependent of lidmaatschapsproduct
    if "optioneleproduct" not in json_body:
        producten = list(OptioneleProducten.objects.all())
        producten = [model_to_dict_remove_id(x) for x in producten]
        response["optioneleproduct"] = random.choice(combs(producten))


    if "surname" not in json_body:
        response["surmame"] = fake.last_name()

    if "initials" not in json_body:
        response["initials"] = "".join(fake.random_letters(length=fake.random_int(1, 6)))
    if "voorvoegsel" not in json_body:
        response["voorvoegsel"] = "".join(fake.random_letters(length=fake.random_int(0, 10)))
    if "birthdate" not in json_body:
        if response["productovereenkomst"]["overeenkomst"] == "Y0":
            birthdate = fake.date_of_birth(
                tzinfo=None, minimum_age=20, maximum_age=24
            ).strftime("%Y-%m-%d")
        else:
            birthdate = fake.date_of_birth(
                tzinfo=None, minimum_age=25, maximum_age=100
            ).strftime("%Y-%m-%d")
        response["birthdate"] = birthdate
    if "postcode" not in json_body:
        response["postcode"] = fake.postcode()
    if "houseNumber" not in json_body:
        response["houseNumber"] = fake.random_int(min=0, max=9999)
    if "houseNumberSuffix" not in json_body:
        response["houseNumberSuffix"] = fake.random_int(min=0, max=9999)
    if "street" not in json_body:
        response["street"] = fake.street_name()
    if "city" not in json_body:
        response["city"] = fake.city()
    if "telefoonnummer" not in json_body:
        response["telefoonnummer"] = "0" + str(fake.random_int(min=111111111, max=999999999))
    if "email" not in json_body:
        response["email"] = fake.free_email()
    if json_body["betaaltermijn"]["termijn"] == "MAAND":
            json_body["automatischeIncasso"] = True
    if "automatischeIncasso" not in json_body:
        response["automatischeIncasso"] = fake.boolean()
    if "iban" not in json_body:
        response["iban"] = fake.iban()
    if "nieuwsbrief" not in json_body:
        response["nieuwsbrief"] = fake.boolean()

    return JsonResponse(response)
