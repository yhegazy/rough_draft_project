from django.forms import ModelForm
from .models import HospitalSite #, AssetTag, ServiceMaxCase

class HospitalSiteForm(ModelForm):
	class Meta:
		model = HospitalSite
		fields = ['Name',]

"""
class AssetTagForm(ModelForm):
	class Meta:
		model = AssetTag
		fields = ['Asset_Number',]

class ServiceMaxCaseForm(ModelForm):
	class Meta:
		model = ServiceMaxCase
		fields = ['Case_Number',]
"""