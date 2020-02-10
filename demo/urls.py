from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from . import views
from .views import status, register, view_profile, edit_profile, change_password
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('status/', status, name='status'),
]

"""
20190723:: I fully do not understand how Django 2.2 path() function works. I understand re_path, or Django 1.X  - url(), and so urlpatterns that should seem to work in path and does not, should be rewritten as a re_path.
"""  
    
urlpatterns += [
    re_path('^$', views.SiteInformationList.as_view()),
    re_path(r'^site/$', views.SiteInformationList.as_view(), name='index'),
    re_path(r'^site/create/$', views.SiteInformationCreate.as_view(), name='record_create'), 
    re_path(r'^site/(?P<pk>\d+)/update/$', views.SiteInformationUpdate.as_view(), name='record_update'),
    re_path(r'^site/(?P<pk>\d+)$',  views.SiteInformationList.as_view(), name='index'),
    re_path(r'^site/details/(?P<pk>\d+)$', views.SiteInformationDetail.as_view(), name='serial_detail'),
    re_path(r'site/register/$', views.register, name='register'),
    re_path(r'site/profile/$', views.view_profile, name='view_profile'),
    re_path(r'site/profile/edit/$', views.edit_profile, name='edit_profile'),
    re_path(r'site/profile/password/$', views.change_password, name='change_password'),
    
    
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    re_path('^accounts/', include('django.contrib.auth.urls')),
    re_path('^pages/', include('django.contrib.flatpages.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 
