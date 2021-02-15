from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import HealthFacilities

# Register your models here.
# class HealthFacilitiesAdmin (admin.OSMGeoAdmin):
#     default_lat = 0.0236
#     default_lon = 37.9062
#     default_zoom = 6
#     # map_template
#     # map_height
#     # modifiable
#     map_width = 750
#     display_raw = True
    
#     fieldsets = (
#         (None, {
#             'fields': ('facility_name', 'county', 'subcounty',
#                        'ward','facility_type','ownership',
#                        'source','geom')}),
#     )    


class HealthFacilitiesAdmin (LeafletGeoAdmin):
    display_raw = True
    list_display = ('facility_name','facility_type','county',)
    list_filter =('facility_type','ownership','county')
    search_fields = ['facility_name']
    fieldsets = (
        (None, {
            'fields': ('facility_name', 'county', 'subcounty',
                       'ward','facility_type','ownership',
                       'source','geom')}),
    )
    
    
admin.site.register(HealthFacilities,HealthFacilitiesAdmin)
#admin.site.register(County, admin.OSMGeoAdmin)

admin.site.site_header = "Health Facility Locator Admin"
admin.site.site_title = "HF Locator"
admin.site.index_title = "Welcome to HFL Portal"
