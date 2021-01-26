from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from .models import HealthFacilities

class HealthFacilityFilter(GeoFilterSet):
    flt_by_type= filters.CharFilter(method= 'get_facilities_by_type')
    flt_by_cnty = filters.CharFilter(method= 'get_facilities_within_county')
    flt_by_sub_cnty = filters.CharFilter(method= 'get_facilities_within_subcounty')
 
    class Meta:
        model = HealthFacilities
        exclude = ['geom']
        
    def get_facilities_within_county(self, queryset, name, value ):
        value = value.capitalize()
        queryset = HealthFacilities.objects.filter(county = value)
        return queryset
    
    def get_facilities_within_subcounty(self, queryset, name, value ):
        queryset = HealthFacilities.objects.filter(subcounty_name__startswith=(value.Capitalize))
        return queryset
    
    def get_facilities_by_type(self, queryset, name, value ):
        queryset = HealthFacilities.objects.filter(facility_type = (value.Capitalize))
        return queryset
    
    
    
    