from django.contrib import admin
from .models import SiteInformation

@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    #https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        (None, {
            'fields': ('Hospital_Name', 'Asset_Number',)
        }),
        ('More options', {
            'classes': ('collapse',),
            'fields': ('Current_Disks', 'Current_CPU', 'Current_RAM', 'Current_Radimetrics_Version', ('Current_OS_Version', 'Type_Of_Server', )),
        }),
    )