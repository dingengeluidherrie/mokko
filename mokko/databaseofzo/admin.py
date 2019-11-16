from django.contrib import admin
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
# Register your models here.
admin.site.register(Lidmaatschapsproducten)
admin.site.register(OptioneleProducten)
admin.site.register(Afspraken)
admin.site.register(Kanaalspecificatiecodes)
admin.site.register(Businessprocessen)
admin.site.register(Geslachten)
admin.site.register(Betaaltermijnen)
admin.site.register(Productovereenkomsten)