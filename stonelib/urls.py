from django.urls import path

from . import views

from stonelib.models import Inscription, Site, Model3D, Image, Museum
from rest_framework import routers, serializers, viewsets
# from rest_framework.views import APIView
# from django.http import JsonResponse
from django.views.generic.detail import DetailView


# Serializers define the API representation.

#list of all inscriptions
class InscriptionSerializer(serializers.HyperlinkedModelSerializer):
    # sites = serializers.StringRelatedField(many=True)
    site_country = serializers.CharField(source='Site.Country')
    site_region = serializers.CharField(source='Site.Region')
    # site_Lat = serializers.FloatField(source='Site.LAT', allow_null = True)
    # site_Lon = serializers.FloatField(source='Site.LON', allow_null = True)
    class Meta:
        model = Inscription
        fields = ['ID', 'Name', 'ContextType', 'site_country','site_region', 'DigitalDocumentation' , 'CitDTS', 'CitVasilev', 'CitBazylhan', 'CitKormushin']
        # 'Country', 'Region',

# ViewSets define the view behavior.
class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

#single inscription
class InscModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3D
        fields = ['ID']

class InscImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['ID', 'Type']
class SingleInscriptionSerializer(serializers.HyperlinkedModelSerializer):
    site_country = serializers.CharField(source='Site.Country')
    site_region = serializers.CharField(source='Site.Region')
    models = InscModelSerializer(many=True)
    images = InscImageSerializer(many=True)
                                     
    class Meta:
        model = Inscription
        fields = ['ID', 'Name','NameVariations', 'ContextType', 'CitDTS', \
         'CitVasilev', 'CitBazylhan','site_country','site_region', 'models', 'images'  ]

class SingleInscriptionView(viewsets.ModelViewSet): 

    queryset = Inscription.objects.all()
    serializer_class = SingleInscriptionSerializer
    # model = Inscription

#list of all sites with all its inscriptions
class InscMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = ['ID', 'Name']

class MapSerializer(serializers.ModelSerializer):

    inscriptions = InscMapSerializer(many=True)

    class Meta:
        model = Site
        fields =  [ 'ID','LAT', 'LON', 'NameToponim', 'NamePerson', 'Type','FirstNotion', 'YearExcavate', 'inscriptions']

class MapView(viewsets.ModelViewSet): 

    queryset = Site.objects.exclude(LAT=None)
    serializer_class = MapSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'inscription', InscriptionViewSet)

urlpatterns = [
    # path('inscription', views.index, name='index'),
    path('inscription', InscriptionViewSet.as_view({'get': 'list'}), name='inscription-list'),
    # path('inscription/<str:ID>/', views.single_inscription, name='single_inscription'),
    path('inscription/<str:pk>/', SingleInscriptionView.as_view({'get': 'retrieve'}), name='inscription-detail'),
    path('map', MapView.as_view({'get': 'list'}), name='map'),  
]