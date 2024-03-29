from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from rest_framework import routers, serializers, viewsets
# from rest_framework.views import APIView
# from django.http import JsonResponse
from django.views.generic.detail import DetailView
from stonelib.models import Inscription, Site, Model3D, Image, Museum

from django.views.generic import View

import os

def index(request):
    print('in index')
    print(request)
    return render(request, 'index.html')



def single_inscription(request, ID):
    
    single_inscription = Inscription.objects.get(ID=ID)

    context = {'inscription': single_inscription}
    
    return render(request, 'stonelib/single_inscription.html', context)

class InscriptionSerializer(serializers.HyperlinkedModelSerializer):
    site_country = serializers.CharField(source='Site.Country')
    site_region = serializers.CharField(source='Site.Region')

    class Meta:
        model = Inscription
        fields = ['ID', 'Name', "NameVariations", 'ContextType', 'site_country','site_region', 'DigitalDocumentation' , 'CitDTS', 'CitVasilev', 'CitBazylhan', 'CitKormushin']


# ViewSets define the view behavior.
class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

#single inscription
class InscModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3D
        fields = ['ID', 'Process', 'Camera', 'Lens', 'FrameCount', 'Scheme',\
                  'Date','Photographer', 'ModelProcesser', 'PolygonCountMaster', 'PolygonCountGeneral','AreaCM', 'Site']

class InscImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['ID', 'Type']

class SingleInscriptionSerializer(serializers.ModelSerializer):
    related_inscriptions = serializers.SerializerMethodField()
    site_country = serializers.CharField(source='Site.Country')
    site_region = serializers.CharField(source='Site.Region')
    models = InscModelSerializer(many=True)
    images = InscImageSerializer(many=True)

    class Meta:
        model = Inscription
        fields = fields = ['ID', 'Name','NameVariations', 'ContextType', 'CitDTS', \
         'CitVasilev', 'CitBazylhan', 'BitigKz', 'site_country','site_region', 'models', 'images',\
'related_inscriptions'  ]
  

    def get_related_inscriptions(self, obj):
        related = Inscription.objects.filter(Site=obj.Site).exclude(ID=obj.ID).values('ID', 'Name')
        return related
# class SingleInscriptionSerializer(serializers.HyperlinkedModelSerializer):


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
