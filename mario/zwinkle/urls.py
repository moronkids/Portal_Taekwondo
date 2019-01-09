# my_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path

from zwinkle import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('create/', views.create, name='create'),
    path('createkrida/', views.krida_create, name='createkrida'),
    path('', views.home_post, name="blog"),
    path('krida/', views.krida, name="krida"),
    re_path(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'^deletekrida/(?P<delete_id_krida>[0-9]+)$', views.deletekrida, name='deletekrida'),
    re_path(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    re_path(r'^updatekrida/(?P<update_id_krida>[0-9]+)$', views.updatekrida, name='updatekrida'),

]