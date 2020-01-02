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

    #20200101Potential uses for later development
    Unit_Sizes = (
        ('-', 'Pick One'),
        ('GB', 'GB'),
        ('MB', 'MB'),
        ('KB', 'KB'),
    )

    Hospital_Name = models.CharField(max_length=250, blank=True, help_text="Hospital Name")
    Asset_Number = models.CharField(max_length=50, blank=False, default="", help_text="ie: 50001201161")
    Current_OS_Version = models.CharField(max_length=10, choices=CURRENT_OS_VERSION, blank=True, default='-', help_text='Current OS Version')
    Current_Radimetrics_Version = models.CharField(max_length=10, blank=False, default='2.9.1b', help_text='ie: 2.9.1b ')
    Type_Of_Server =  models.CharField(max_length=20, choices=TYPE_OF_SERVER, blank=False, default='-', help_text='Server Type')
    Current_Disks = models.CharField(max_length=50, blank=False, default="", help_text="ie: 100/100/200")
    Current_CPU = models.CharField(max_length=5, blank=False, default="", help_text="ie: 4")
    Current_RAM = models.CharField(max_length=5, blank=False, default="", help_text="ie: 16GB")
    DB_Version = models.CharField(max_length=5, blank=True, default="", help_text="ie: 8.4")
    ExposureDB_Size = models.CharField(max_length=50, blank=True, default="", help_text="ie: 26GB, 600MB, 1000KB")
    MirthDB_Size = models.CharField(max_length=50, blank=True, default="", help_text="ie: 5GB, 857MB")
    Site_Hostname = models.CharField(max_length=100, blank=True, default="", help_text="ie: eXposure.domain.local")
    Site_IP_Address = models.CharField(max_length=100, blank=True, default="", help_text="ie: 127.0.0.1")
    Notes = models.TextField(max_length=1250, blank=True, default="")
 
    #Case_Number_Details = models.ForeignKey(ServiceMaxCase, on_delete=models.SET_NULL, null=True, help_text="Case Number Details")

    class Meta:
        ordering = ["Hospital_Name"]

    def __str__(self):
        return self.Hospital_Name
    
    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])

class AccountInformation(models.Model): 
    Account_Name = models.CharField(max_length=250, blank=True, help_text="Site Account Name")
    Exposure_Number = models.CharField(max_length=250, blank=True, help_text="EXPOSURE-[] ie EXPOSURE-919238")

    class Meta:
       ordering = ["Account_Name"]

    def __str__(self):
        return self.Account_Name
    
    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])


class Account(models.Model): 
    Account_Name = models.OneToOneField(AccountInformation, on_delete=models.SET_NULL, null=True, blank=True)
    Site_Name = models.OneToOneField(SiteInformation, on_delete=models.SET_NULL, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])

