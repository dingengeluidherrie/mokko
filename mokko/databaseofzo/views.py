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
from .utils import combs
from faker import Faker
import random
from django.forms.models import model_to_dict
from itertools import combinations
import json

# Create your views here.
fake = Faker("nl_NL")


@csrf_exempt
def dingen(request):

    json_body = json.loads(request.body)
    response = json_body

    if "lidmaatschapsproduct" not in json_body:
        response["lidmaatschapsproduct"] = model_to_dict(
            Lidmaatschapsproducten.objects.order_by("?").first()
        )
    if "afspraken" not in json_body:
         afspraken = list(Afspraken.objects.all())
         afspraken = [None] + [model_to_dict(x) for x in afspraken]
         choice = random.choice(afspraken)
         if choice is not None:
            response["afspraken"] = choice
    if "businessproces" not in json_body:
        response["businessproces"] = model_to_dict(
            Businessprocessen.objects.order_by("?").first()
        )
    if "kanaalspecificatiecode" not in json_body:
        response["kanaalspecificatiecode"] = model_to_dict(
            Kanaalspecificatiecodes.objects.order_by("?").first()
        )
    if "productovereenkomst" not in json_body:
        response["productovereenkomst"] = model_to_dict(
            Productovereenkomsten.objects.order_by("?").first()
        )    
    if "betaaltermijn" not in json_body:
        response["betaaltermijn"] = model_to_dict(
            Betaaltermijnen.objects.order_by("?").first()
        )    
    if "gender" not in json_body:
        response["gender"] = model_to_dict(
            Geslachten.objects.order_by("?").first()
        )                  
    if "optioneleproduct" not in json_body:
        producten = list(OptioneleProducten.objects.all())
        producten = [model_to_dict(x) for x in producten]
        response["optioneleproduct"] = random.choice(combs(producten))
    if "surname" not in json_body:
        response["surmame"] = fake.last_name()
    return JsonResponse(response)
