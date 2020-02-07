from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from .models import SiteInformation
from .forms import RegistrationForm

def home(request):
    return render(request, "index.html", {})

    
def status(request):
    #example = ModelName.objects.annotate(Count('authors'), Count('store'))
    server_count = SiteInformation.objects.all().count()
    current_release_count = SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.9").count()

    
    #20200205::This next set of lines are hardcoded until I can find a better way of doing this. 
    
    sum_of_outdated = (SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.8").count() + SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.7").count() + SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.6").count() + 
    SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.5").count())

    sum_of_deprecated = (SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.4").count() + SiteInformation.objects.filter(Current_Radimetrics_Version__contains="2.3").count())
    
    #Version Numbers Individualized
    #Current
    ver291b = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.9.1b").count()
    ver29b = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.9b").count()
   
    #Outdated
    ver28b = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.8b").count()
    ver271 = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.7.1").count()
    ver27a = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.7a").count()
    ver26b = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.6b").count()
    ver251b = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.5.1b").count()
    ver25a = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.5a").count()

    #Deprecated/Obsolete
    ver24a = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.4a").count()
    ver23a = SiteInformation.objects.filter(Current_Radimetrics_Version__exact="2.3a").count()

    #Table for OS Version
    rhel = SiteInformation.objects.filter(Current_OS_Version__exact='RedHat').count()
    suse = SiteInformation.objects.filter(Current_OS_Version__exact='OpenSuse').count()
    cent = SiteInformation.objects.filter(Current_OS_Version__exact='CentOS').count()

    context={
        'server_count':server_count,
        'current_release_count': current_release_count,
        'sum_of_outdated': sum_of_outdated,
        'sum_of_deprecated': sum_of_deprecated,
        'ver291b': ver291b,
        'ver29b': ver29b,
        'ver28b': ver28b,
        'ver271': ver271,
        'ver27a': ver27a,
        'ver26b': ver26b,
        'ver251b': ver251b,
        'ver25a': ver25a,
        'ver24a': ver24a,
        'ver23a': ver23a,
        'rhel': rhel,
        'suse': suse,
        'cent': cent,
    }


    return render(request, "status.html", context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hospitalsite')
    else:
        form = RegistrationForm()

        context = {'form': form}
        return render(request, 'registration/reg_form.html', context)



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
    fields = ['Site_Name', 'Serial_Number', 'Decommission', 'Serial_Removed', 'Current_Radimetrics_Version', 'Type_Of_Server', 'Notes', 'Site_Hostname', 'Site_IP_Address', 'Current_OS_Version', 'Disk_1', 'Disk_2', 'Disk_3', 'Current_CPU', 'Current_RAM', 'DB_Version', 'DB_Size1', 'DB_Size2' ]