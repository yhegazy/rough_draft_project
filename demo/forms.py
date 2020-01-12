from django.forms import ModelForm
from .models import SiteInformation

class SiteInformationForm(ModelForm):
	class Meta:
		model = SiteInformation

class SiteInformationView(FormView):
	model = SiteInformation
	template_name = 'record_update.html'
	success_url = reverse_lazy('record_update')

    def form_valid(self, form):
        SiteInformation.objects.update_or_create(
            'Site_Name': form.cleaned_data["Site_Name"]
            defaults={
                'Serial_Number': form.cleaned_data["Serial_Number"],
                'Current_Radimetrics_Version': form.cleaned_data["Current_Radimetrics_Version"],
                'Type_Of_Server': form.cleaned_data['Type_Of_Server'],  
                'Current_Disks':form.cleaned_data['Current_Disks'], 
				'Current_CPU':form.cleaned_data['Current_CPU'], 
				'Current_RAM':form.cleaned_data['Current_RAM'],  
            }
        )
        return render(self.request, self.template_name, {'form': form})