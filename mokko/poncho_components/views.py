from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import PonchoComponents
from .ding import ding
import gitlab
import re

# Create your views here.


@csrf_exempt
def update_component_table(request):

    gl = gitlab.Gitlab(
        "https://gitlab.anwbonline.nl/", private_token="eteXYxTEbF8bJJR__67A"
    )
    project = gl.projects.get(238)
    componentlist = [
        (x["name"], x["path"] + "/src/")
        for x in project.repository_tree(path="packages/components", all=True)
    ]
    for component in componentlist:
        # TODO: check for differences in the props of the component
        if PonchoComponents.objects.filter(componentname=component[0]).count() == 0:
            c = PonchoComponents(componentname=component[0])
            c.save()
        for ponchofile in project.repository_tree(path=component[1], all=True):
            name = ponchofile["name"]
            pattern = re.compile("(\.stories\.|index\.js)")
            if not re.search(pattern, name) and name.endswith(".js"):
                poncho_file = project.files.get(
                    file_path=component[1] + name, ref="master"
                )
                decoded_poncho_file = poncho_file.decode()
                print(component[1] + name)
                prop_array = ding(decoded_poncho_file.decode().split("\n"))
                # print(prop_array)
                print([key for key, value in prop_array.items() if value.lower() == 'boolean'])
                # print(dict(element.split(':') for element in prop_array))
