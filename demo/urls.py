from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home
from . import views

urlpatterns = [
    path('demo/', home, name='home'),
    path('admin/demo/', admin.site.urls),
    path('demo/', include('django.contrib.auth.urls')),

]

"""
20190723:: I fully do not understand how Django 2.2 path() function works. I understand re_path, or Django 1.X  - url(), and so urlpatterns that should seem to work in path and does not, should be rewritten as a re_path.
"""  
    
urlpatterns += [
    re_path(r'^hospitalsite/$', views.HospitalSiteList.as_view(), name='test'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 
