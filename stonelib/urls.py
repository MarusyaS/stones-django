from django.urls import path
from django.views.generic import TemplateView
from . import views

from django.conf import settings
from django.conf.urls.static import static



# Serializers define the API representation.

#list of all inscriptions

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'inscription', InscriptionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('inscription', views.InscriptionViewSet.as_view({'get': 'list'}), name='inscription-list'),
    # path('inscription/<str:ID>/', views.single_inscription, name='single_inscription'),
    path('inscription/<str:pk>/', views.SingleInscriptionView.as_view({'get': 'retrieve'}), name='inscription-detail'),
    path('map', views.MapView.as_view({'get': 'list'}), name='map'),
]
