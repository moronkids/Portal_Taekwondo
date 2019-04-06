# my_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
app_name = 'zwinkle'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('create/', views.create, name='create'),
    path('krida/ujian', views.Ujian.as_view(), name='ujian'),
    path('', views.home_post, name="blog"),
    path('krida/about/', views.about_krida, name="about_krida"),
    re_path(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
	path('krida/daftar_peserta', views.HomepageView.as_view(), name='homepage'),
	path('krida/<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('krida/create/', views.CollectionCreate.as_view(), name='collection_create'),
    path('krida/update/<int:pk>/', views.CollectionUpdate.as_view(), name='collection_update'),
    path('krida/delete/<int:pk>/', views.CollectionDelete.as_view(), name='collection_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)