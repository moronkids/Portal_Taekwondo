# my_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path

from zwinkle import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('create/', views.create, name='create'),
    path('', views.home_post, name="blog"),
    re_path(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),

]