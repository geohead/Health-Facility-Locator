from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import HttpResponse, render

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action
from django_filters import rest_framework  as filters

from .locator_serializer import HealthFacilitiesSerializer
from .locator_filter import HealthFacilityFilter
from .models import HealthFacilities

# Create your views here.

def indexView(request):
    
    return render(request,'locator/home.html')


def contactView(request):
    mssg ="For queries contact me at bonairhassan@gmail.com "
    return HttpResponse(mssg)

def aboutView(request):
    mssg ="This app shows details about health facilities in Kenya. "
    return HttpResponse(mssg)





class HealthFacilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = HealthFacilitiesSerializer
    queryset = HealthFacilities.objects.all()
    filterset_class = HealthFacilityFilter
    filter_backends = [filters.DjangoFilterBackend]
    
    @action(detail=False, methods=['get'])
    def get_nearest_facilities(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords),srid=4326)
            nearest_five_facilities = HealthFacilities.objects.annotate(distance=Distance('geom',user_location)).order_by('distance')[:8]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_five_facilities, many = True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)



