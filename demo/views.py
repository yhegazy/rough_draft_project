from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SiteInformation, AccountInformation, Account
from django.http import HttpResponseRedirect

def home(request):
	return render(request, "index.html", {})

class SiteInformationList(generic.ListView):
	model = SiteInformation
	context_object_name = 'siteinformation' 
	template_name = 'index.html'

	paginate_by = 10

class SiteInformationDetail(generic.DetailView):
    model = SiteInformation

class SiteInformationCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = SiteInformation
    fields = '__all__'

class SiteInformationUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'

    model = SiteInformation
    #Display only the fields that you would like to update
    fields = ['Hospital_Name', 'Asset_Number', 'Current_Disks', 'Current_CPU', 'Current_RAM', 'Current_Radimetrics_Version', 'Current_OS_Version', 'Type_Of_Server', 'DB_Version', 'ExposureDB_Size', 'MirthDB_Size', 'Site_Hostname', 'Site_IP_Address', 'Notes' ]

class AccountInformationList(generic.ListView):
	model = AccountInformation
	context_object_name = 'accountinformation' 
	template_name = 'index.html'

	#paginate_by = 10

class AccountList(generic.ListView):
	model = Account

	context_object_name = 'account' 
	template_name = 'index.html'
	queryset = Account.objects.all()
	
	def get_context_data(self, **kwargs):
		#Call the views to be displayed onto the template
		context = super(Account, self).get_context_data(**kwargs)
		context['site_info'] = SiteInformation.objects.all()
		context['acc_info'] = AccountInformation.objects.all()
		return context
		