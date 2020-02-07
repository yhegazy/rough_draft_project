from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL pattern
from PIL import Image

class SiteInformation(models.Model):
    #do drop down builds here:
    CURRENT_OS_VERSION = (
        ('-', 'Pick One'),
        ('RedHat', 'RedHat'),
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

    Site_Name = models.CharField(max_length=100, blank=True, help_text="Hospital Name")
    Serial_Number = models.CharField(max_length=50, blank=False, default="", help_text="ie: 50001201161")
    Current_OS_Version = models.CharField(max_length=10, choices=CURRENT_OS_VERSION, blank=True, default='-', help_text='Current OS Version')
    Current_Radimetrics_Version = models.CharField(max_length=10, blank=False, default='2.9.1b', help_text='ie: 2.9.1b ')
    Type_Of_Server =  models.CharField(max_length=20, choices=TYPE_OF_SERVER, blank=False, default='-', help_text='Server Type')
    Disk_1 = models.CharField(max_length=50, blank=False, default="100")
    Disk_2 = models.CharField(max_length=50, blank=False, default="100")
    Disk_3 = models.CharField(max_length=50, blank=False, default="200")
    Current_CPU = models.CharField(max_length=5, blank=False, default="", help_text="ie: 4")
    Current_RAM = models.CharField(max_length=5, blank=False, default="", help_text="ie: 16")
    DB_Version = models.CharField(max_length=10, blank=True, default="", help_text="ie: 8.4")
    DB_Size1 = models.CharField(max_length=50, blank=True, default="50", help_text="ie: 100GB")
    DB_Size2 = models.CharField(max_length=50, blank=True, default="", help_text="ie: 5")
    Site_Hostname = models.CharField(max_length=100, blank=True, default="", help_text="ie: hostname.domain.local")
    Site_IP_Address = models.CharField(max_length=100, blank=True, default="", help_text="ie: 127.0.0.1")
    Notes = models.TextField(max_length=1250, blank=True, default="")
    Decommission = models.BooleanField(default=False)
    Serial_Removed = models.BooleanField(default=False)
 
    #Case_Number_Details = models.ForeignKey(ServiceMaxCase, on_delete=models.SET_NULL, null=True, help_text="Case Number Details")

    class Meta:
        ordering = ["Site_Name"]


    def __str__(self):
        return self.Hospital_Name
    
    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])
