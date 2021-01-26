from django.urls import path, include
from rest_framework import routers

from .views import aboutView, contactView, indexView, HealthFacilitiesViewSet


router = routers.DefaultRouter()
router.register(r'healthfacilities', HealthFacilitiesViewSet )


urlpatterns =[
    
    path('',indexView,name='Index'),
    path('api/', include(router.urls)),
    path('about/', aboutView, name= 'about'),
    path('contact/', contactView, name= 'contact_us'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    ]