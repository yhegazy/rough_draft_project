from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL pattern
from PIL import Image

class SiteInformation(models.Model):
    #do drop down builds here:
    CURRENT_OS_VERSION = (
        ('-', 'Pick One'),
        ('RedHat', 'RHEL'),
        ('OpenSuse', 'OpenSuse'),
        ('CentOS', 'CentOS'),
    )

    TYPE_OF_SERVER = (
        ('-', 'Pick One'),
        ('PROD', 'PROD'),
        ('TEST', 'TEST'),
        ('CONTRAST', 'CONTRAST ONLY'),
        ('PREPROCESSOR', 'PRE-PROCESSOR'),
        ('ENTERPRISE', 'ENTERPRISE'),
        ('APP', 'APP'),
        ('DB', 'DB'),
    )

    Hospital_Name = models.CharField(max_length=250, blank=True, help_text="Hospital Name")
    Asset_Number = models.CharField(max_length=50, blank=False, default="", help_text="ie: 50001201161")
    Current_OS_Version = models.CharField(max_length=10, choices=CURRENT_OS_VERSION, blank=True, default='-', help_text='Current OS Version')
    Current_Radimetrics_Version = models.CharField(max_length=10, blank=False, default='2.9.1b', help_text='ie: 2.9.1b ')

  
    Type_Of_Server =  models.CharField(max_length=20, choices=TYPE_OF_SERVER, blank=False, default='-', help_text='Server Type')

    Current_Disks = models.CharField(max_length=50, blank=False, default="", help_text="ie: 100/100/200")
    Current_CPU = models.CharField(max_length=5, blank=False, default="", help_text="ie: 4")
    Current_RAM = models.CharField(max_length=5, blank=False, default="", help_text="ie: 16")
    
  
    #Current_Radimetrics_Requirements = models.CharField(max_length=10, blank=False, default='2.9.1b', help_text='Color Coded Red for current_rad_version=<2.4a, Yellow for current_rad_version=<2.9b and Green for current_rad_version == minimum_rad_version')
 
    #Case_Number_Details = models.ForeignKey(ServiceMaxCase, on_delete=models.SET_NULL, null=True, help_text="Case Number Details")

    class Meta:
        ordering = ["Hospital_Name"]


    def __str__(self):
        return self.Hospital_Name
    
    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])
