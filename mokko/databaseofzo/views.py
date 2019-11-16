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
    if "optioneleproduct" not in json_body:
        producten = list(OptioneleProducten.objects.all())
        producten = [model_to_dict(x) for x in producten]
        response["optioneleproduct"] = random.choice(combs(producten))
    if "surname" not in json_body:
        response["surmame"] = fake.last_name()
    return JsonResponse(response)
