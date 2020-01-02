from django.forms import ModelForm
from .models import SiteInformation

class SiteInformationForm(ModelForm):
	class Meta:
		model = SiteInformation
