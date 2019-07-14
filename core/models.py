from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL pattern
from PIL import Image

# Create your models here. From bottm up (detail -> general)
class ServiceMaxCase(models.Model):
    #Drop Down Builds
    WO_TYPE = (
        ('VSS', 'VSS'),
        ('VCU', 'VCU'),
    )

    UPGRADED_BY = (
        ('Heath', 'Heath Guy'),
        ('Yahia', 'Yahia Hegazy'),
    )

    Case_Number = models.CharField(max_length=100, blank=True, help_text="ie: 0067824")
    WO_Type = models.CharField(max_length=3, choices=WO_TYPE, blank=True, default='-', help_text='Work Order Type')
    UPA = models.BooleanField() 
    Minimum_Server_Requirements = models.BooleanField()

    Minimum_Radimetrics_Requirements = models.CharField(max_length=10, blank=False, default='2.9.1b', help_text='Color Coded Red for current_rad_version<2.7a, Yellow for current_rad_version<2.9b and Green for current_rad_version == minimum_rad_version')

    Primary_Email = models.CharField(max_length=100, blank=True, help_text='Primary Email')
    Clinical_Email = models.CharField(max_length=100, blank=True, help_text='Clinical Email')
    
    Scheduled_Upgrade_Date = models.DateField(null=True, blank=True)
    Contacted_Customer = models.BooleanField()
    Followed_Up_With_Customer = models.BooleanField()
    Followed_Up_With_Customer_Date = models.DateField(null=True, blank=True)
    
    Upgrade_Complete = models.BooleanField(default=False)
    Upgrade_Date = models.DateField(null=True, blank=True)
    Upgrade_Total_Time = models.IntegerField(default=0)
    Upgraded_By = models.CharField(max_length=10, choices=UPGRADED_BY, default='-') 

    
    DoseCalc_Suppression = models.BooleanField()
    IP_Page_Updated = models.BooleanField()    
    SDI_Count = models.IntegerField(default=0)
   
    Notes = models.TextField(max_length=250, blank=True, help_text='Notes - Server Pre-Check')
    
    def __str__(self):
       return self.Case_Number


class AssetTag(models.Model):
    #do drop down builds here:
    CURRENT_OS_VERSION = (
        ('-', 'Pick One'),
        ('RedHat', 'RHEL'),
        ('OpenSuse', 'OpenSuse'),
        ('CentOS', 'CentOS'),
    )
    TYPE_OF_SERVER = (
        ('-', 'Pick One'),
        ('Prod', 'PROD'),
        ('Test', 'TEST'),
        ('Contrast', 'CONTRAST ONLY'),
        ('Pre-Processor', 'PRE-PROCESSOR'),
        ('Enterprise', 'ENTERPRISE'),
    )

    Asset_Number = models.CharField(max_length=50, blank=False, default="", help_text="ie: 50001201161")
    Current_OS_Version = models.CharField(max_length=10, choices=CURRENT_OS_VERSION, blank=True, default='-', help_text='Current OS Version')
    Current_Radimetrics_Version = models.CharField(max_length=10, blank=False, default='2.9.1b', help_text='Current Radimetrics Version ')
    Type_Of_Server =  models.CharField(max_length=20, choices=TYPE_OF_SERVER, blank=False, default='-', help_text='Type of Server')

    Current_Disks = models.CharField(max_length=50, blank=False, default="", help_text="ie: 100/100/200")
    Current_CPU = models.CharField(max_length=1, blank=False, default="", help_text="ie: 4")
    Current_RAM = models.CharField(max_length=5, blank=False, default="", help_text="ie: 16")
    
    """
    @property
    def os_check(self):
        for os in self.CURRENT_OS_VERSION:
            if os == 'RedHat':
                self.RedHat_Subscription = models.BooleanField(help_text="Subscribed?")
             
                return self.RedHat_Subscription
    """
    Case_Number_Details = models.ForeignKey(ServiceMaxCase, on_delete=models.SET_NULL, null=True, help_text="Case Number Details")

    def __str__(self):
        return self.Asset_Number

class HospitalSite(models.Model):
    Name = models.CharField(max_length=100, blank=True, help_text="Hospital Name")
    Asset_Tag_Information = models.ManyToManyField(AssetTag, help_text="Asset Tag Information")

    def __str__(self):
        return self.Name

