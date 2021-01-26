from django.contrib.gis.db import models




class HealthFacilities(models.Model):
    
    OWNERSHIP_CHOICES = [
        ('NGO','NGO'),
        ('FBO','FBO'),
        ('MoH','MoH'),
        ('Local Authority','Local Authority'),
        ('Private','Private'),
    ]

    FACILITY_TYPE_CHOICES =[
        ('Clinic','Clinic'),
        ('Dispensary','Dispensary'),
        ('District Hospital','District Hospital'),
        ('Health Centre','Health Centre'),
        ('Misssion Hospital','Misssion Hospital'),
        ('National Referral Hospital','National Referral Hospital'),
        ('Provincial General Hospital','Provincial General Hospital'),
        ('Sub-District Hospital','Sub-District Hospital'),
    ]
    SOURCE_CHOICES = [
        ('GPS','GPS'),
        ('Google Earth','Google Earth'),
        ('Other','Other'),
        ('Geonames','Geonames')
        
    ]

    facility_name = models.CharField(max_length=70, null= False)
    county = models.CharField(max_length=35, null= False)
    subcounty = models.CharField(max_length =40, null= False)
    ward = models.CharField(max_length =40, null= False)
    facility_type = models.CharField(max_length=30, choices= FACILITY_TYPE_CHOICES, null= False)
    ownership = models.CharField(max_length=15, choices= OWNERSHIP_CHOICES, null= False)
    source = models.CharField(max_length=15, choices= SOURCE_CHOICES)
    geom = models.MultiPointField(srid=4326)
    
    def __str__(self):
        return self.facility_name
    
    class Meta:
        verbose_name = "Health Faclity"
        verbose_name_plural = "Health Facilities"
        indexes = [models.Index(fields=['facility_name'])]
                   
  
