from django.urls import path

from . import views

from stonelib.models import Inscription, Site
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class InscriptionSerializer(serializers.HyperlinkedModelSerializer):
    # sites = serializers.StringRelatedField(many=True)
    site_country = serializers.CharField(source='Site.Country')
    site_region = serializers.CharField(source='Site.Region')
    class Meta:
        model = Inscription
        fields = ['ID', 'Name', 'ContextType', 'site_country','site_region', 'DigitalDocumentation' ]
        # 'Country', 'Region',

# ViewSets define the view behavior.
class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'inscription', InscriptionViewSet)

urlpatterns = [
    # path('inscription', views.index, name='index'),
    path('inscription', InscriptionViewSet.as_view({'get': 'list'})),
    path('inscription/<str:ID>/', views.single_inscription, name='single_inscription'),
]