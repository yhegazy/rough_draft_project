from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import views
from .views import home

urlpatterns = [
    path('admin/demo/', admin.site.urls),
    path('', home, name='home'),
   # path('core.ServiceMaxCaseListView/servicemaxcase_list', views.ServiceMaxCaseListView.as_view(), name='servicemaxcase_list')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 
