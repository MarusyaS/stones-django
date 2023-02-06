from django.urls import path

from . import views

from stonelib.models import Inscription, Site
from rest_framework import routers, serializers, viewsets
# from rest_framework.views import APIView
# from django.http import JsonResponse
from django.views.generic.detail import DetailView


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

class SingleInscriptionSerializer(serializers.HyperlinkedModelSerializer):
    site_country = serializers.CharField(source='Site.Country')
    site_region = serializers.CharField(source='Site.Region')
    class Meta:
        model = Inscription
        fields = ['ID', 'Name','NameVariations', 'ContextType', 'CitDTS', \
         'CitVasilev', 'CitBazylhan','site_country','site_region'  ]

class SingleInscriptionView(viewsets.ModelViewSet): 

    queryset = Inscription.objects.all()
    serializer_class = SingleInscriptionSerializer
    # model = Inscription


# class SingleInscriptionView(APIView):      
#     def get_objects(self,nm):
#         try: 
#             return Inscription.objects.get(pk = nm)
#         except Inscription.DoesNotExist:
#             raise Http404('Not found')


#     def get(self,request,nm,format =None):
#         item = self.get_objects(nm)
#         serializer = SingleInscriptionSerializer(item)
#         return JsonResponse(serializer.data)

#         return HttpResponse(status =status.HTTP_204_NO_CONTENT)

    # queryset = Inscription.objects.select_related('Site').get(id=ID)


# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'inscription', InscriptionViewSet)

urlpatterns = [
    # path('inscription', views.index, name='index'),
    path('inscription', InscriptionViewSet.as_view({'get': 'list'}), name='inscription-list'),
    # path('inscription/<str:ID>/', views.single_inscription, name='single_inscription'),
    path('inscription/<str:pk>/', SingleInscriptionView.as_view({'get': 'retrieve'}), name='inscription-detail'),
    
]