from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HospitalSite
	
def home(request):
	return render(request, "index.html", {})


class HospitalSiteList(generic.ListView):
	model = HospitalSite
	context_object_name = 'test' 
	template_name = 'index.html'


	