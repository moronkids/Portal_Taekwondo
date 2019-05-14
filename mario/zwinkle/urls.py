# my_project/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .views import AnggotaAutocomplete, KridaAutocomplete, TestModelList, TestModelListJson, IndexView
app_name = 'zwinkle'
urlpatterns = [
                  url(r'^testmodel$', TestModelList.as_view(), name="testmodel"),
                  url(r'^cek$', IndexView.as_view(), name="index"),
                  url(r'^testmodel_data/$', TestModelListJson.as_view(), name="testmodel_list_json"),
    path('admin/', admin.site.urls),
    path('create/', views.create, name='create'),
    path('krida/ujian', views.ujian, name='ujian'),
    path('', views.home_post, name="blog"),
    re_path(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
	path('krida/daftar_peserta', views.base, name='homepage'),
	path('krida/about', views.about, name='about'),
	path('krida/nilai', views.nilai, name='nilai'),
	path('krida/<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
	path('krida2/<int:pk>/', views.CollectionDetailView.as_view(), name='anggota_detail'),
    path('krida/create-anggota/', views.AnggotaCreate.as_view(), name='anggota_create'),
    path('krida/create-peserta-ujian/', views.CollectionCreate.as_view(), name='collection_create'),
    path('krida/update_ujian/<int:pk>/', views.CollectionUpdate.as_view(), name='collection_update'),
    path('krida/update_anggota/<int:pk>/', views.AnggotaUpdate.as_view(), name='anggota_update'),
    path('krida/delete/<int:pk>/', views.CollectionDelete.as_view(), name='collection_delete'),
    path('krida/delete/anggota/<int:pk>/', views.AnggotaDelete.as_view(), name='anggota_delete'),
    path(
        r'anggota-autocomplete/',
        AnggotaAutocomplete.as_view(),
        name='anggota-autocomplete',
    ),

    path(
        r'krida-autocomplete/',
        KridaAutocomplete.as_view(),
        name='krida-autocomplete',
    ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)