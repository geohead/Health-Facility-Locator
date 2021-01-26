from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import HealthFacilities, County


facilities_mapping = {
    
    'facility_name':'Facility_n',
    'county':'Admin1',
    'subcounty':'subcounty',
    'ward':'ward',
    'facility_type':'Facility_t',
    'ownership':'Ownership',
    'source':'LL_source',
    'geom':'MULTIPOINT',
}

health_facilities_shp = Path(__file__).resolve().parent / 'datasets' / 'health_facilities_ke.shp'

def run(verbose=True):
    lm = LayerMapping(HealthFacilities, str(health_facilities_shp), facilities_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
    
