from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('(?P<item_id>\d{1,})/(?P<tab_id>\d{1,})', views.item),
    path('map', views.map),
    path('items', views.items),
    path('(?P<item_id>\d{1,})/video/(?P<video_id>\d{1,})', views.video),
]