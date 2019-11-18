from rest_framework import routers, serializers, viewsets
from .models import (
    PonchoComponents,
)

class PonchoComponentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PonchoComponents
        fields = ['url', 'componentname']

# ViewSets define the view behavior.
class PonchoComponentsViewSet(viewsets.ModelViewSet):
    queryset = PonchoComponents.objects.all()
    serializer_class = PonchoComponentsSerializer

