from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import home
from demo import views

urlpatterns = [
    path('admin/demo/', admin.site.urls),
    path('', home, name='home'),
  #  path('ServiceMaxCaseListView', views.ServiceMaxCaseListView.as_view(), name='demo/servicemaxcase_list')
    path('demo/', include('django.contrib.auth.urls'))
   
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 
