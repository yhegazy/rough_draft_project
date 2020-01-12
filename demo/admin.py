from django.contrib import admin
from .models import SiteInformation

@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    #https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        (None, {
            'fields': ('Site_Name', 'Serial_Number', 'Decommission', 'Serial_Removed', 'Current_Radimetrics_Version', 'Type_Of_Server', 'Notes')
        }),
        ('Server Type Details ', {
            'fields': ('Site_Hostname', 'Site_IP_Address', 'Current_OS_Version', 'Disk_1', 'Disk_2', 'Disk_3', 'Current_CPU', 'Current_RAM', 'DB_Version', ('ExposureDB_Size', 'MirthDB_Size', )),
        }),
    )