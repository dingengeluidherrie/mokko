from rest_framework import routers, serializers, viewsets
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

class LidmaatschapsproductenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lidmaatschapsproducten
        fields = ['url', 'productnaam', 'productcode', 'graad', 'dekking']

# ViewSets define the view behavior.
class LidmaatschapsproductenViewSet(viewsets.ModelViewSet):
    queryset = Lidmaatschapsproducten.objects.all()
    serializer_class = LidmaatschapsproductenSerializer

class OptioneleProductenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OptioneleProducten
        fields = ['url', 'productcode']

class OptioneleProductenViewSet(viewsets.ModelViewSet):
    queryset = OptioneleProducten.objects.all()
    serializer_class = OptioneleProductenSerializer

class AfsprakenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Afspraken
        fields = ['url', 'afspraak']

# ViewSets define the view behavior.
class AfsprakenViewSet(viewsets.ModelViewSet):
    queryset = Afspraken.objects.all()
    serializer_class = AfsprakenSerializer

class KanaalspecificatiecodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kanaalspecificatiecodes
        fields = ['url', 'spec']

class KanaalspecificatiecodesViewSet(viewsets.ModelViewSet):
    queryset = Kanaalspecificatiecodes.objects.all()
    serializer_class = KanaalspecificatiecodesSerializer

class BetaaltermijnenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Betaaltermijnen
        fields = ['url', 'termijn']

# ViewSets define the view behavior.
class BetaaltermijnenViewSet(viewsets.ModelViewSet):
    queryset = Betaaltermijnen.objects.all()
    serializer_class = BetaaltermijnenSerializer

class BusinessprocessenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Businessprocessen
        fields = ['url', 'proces']

class BusinessprocessenViewSet(viewsets.ModelViewSet):
    queryset = Businessprocessen.objects.all()
    serializer_class = BusinessprocessenSerializer


class GeslachtenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geslachten
        fields = ['url', 'geslacht']

# ViewSets define the view behavior.
class GeslachtenViewSet(viewsets.ModelViewSet):
    queryset = Geslachten.objects.all()
    serializer_class = GeslachtenSerializer

class ProductovereenkomstenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productovereenkomsten
        fields = ['url', 'overeenkomst']

class ProductovereenkomstenViewSet(viewsets.ModelViewSet):
    queryset = Productovereenkomsten.objects.all()
    serializer_class = ProductovereenkomstenSerializer