from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import HealthFacilities


class HealthFacilitiesSerializer (GeoFeatureModelSerializer):
    
    class Meta:
        
        model = HealthFacilities
        geo_field = 'geom'
        
        fields = ('facility_name', 'county', 'subcounty',\
            'ward','facility_type','ownership','geom')
        

