from django.shortcuts import render
from django.views import generic
from .models import ServiceMaxCase
	
def home(request):
    return render(request, "index.html", {})


class ServiceMaxCaseListView(generic.ListView):
		model = ServiceMaxCase
      #  context_object_name = 'my_servicemaxcase_list' # your own name for the list as a template variable
		queryset = model.objects.filter(Case_Number__icontains='insert random meaningful word here')
		template_name = 'demo/servicemaxcase_list.html' # Specify your own template name/location