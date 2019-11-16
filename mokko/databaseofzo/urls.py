"""mokko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .models import Lidmaatschapsproducten
from .views import dingen
from .serializers import (
    LidmaatschapsproductenViewSet,
    OptioneleProductenViewSet,
    AfsprakenViewSet,
    KanaalspecificatiecodesViewSet,
    BetaaltermijnenViewSet,
    BusinessprocessenViewSet,
    GeslachtenViewSet,
    ProductovereenkomstenViewSet,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'lidmaatschapsproducten', LidmaatschapsproductenViewSet)
router.register(r'optioneleproducten', OptioneleProductenViewSet)
router.register(r'afspraken', AfsprakenViewSet)
router.register(r'kanaalspecificatiecodes', KanaalspecificatiecodesViewSet)
router.register(r'betaaltermijnen', BetaaltermijnenViewSet)
router.register(r'businessprocessen', BusinessprocessenViewSet)
router.register(r'geslachten', GeslachtenViewSet)
router.register(r'productovereenkomsten', ProductovereenkomstenViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('dingen/', dingen),
]
