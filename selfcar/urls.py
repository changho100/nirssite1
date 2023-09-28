from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.selfcar),
    url(r'^selfcar_insert$', views.selfcar_insert),
    url(r'^selfcar_comf$', views.selfcar_comf),
    url(r'^exe_selfcar$', views.exe_selfcar),
    url(r'^exe_search_selfcar$', views.exe_search_selfcar),
    url(r'^exe_delete_selfcar/(?P<selfcarid>\d{1,})$', views.exe_delete_selfcar),
    url(r'^selfcar_reject$', views.selfcar_reject),
    url(r'^selfcar_admin$', views.selfcar_admin),
    url(r'^exe_list_selfcar$', views.exe_list_selfcar),
]