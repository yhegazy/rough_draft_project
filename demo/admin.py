from django.contrib import admin
from .models import HospitalSite, AssetTag, ServiceMaxCase

@admin.register(HospitalSite)
class HospitalSiteAdmin(admin.ModelAdmin):
    pass

@admin.register(AssetTag)
class AssetTagAdmin(admin.ModelAdmin):
    pass

@admin.register(ServiceMaxCase)
class ServiceMaxCaseAdmin(admin.ModelAdmin):
    pass