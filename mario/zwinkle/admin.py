from django.contrib import admin

# Register your models here.
from .models import konten, buat_login, Publication, Article

admin.site.register(konten)
admin.site.register(buat_login)
admin.site.register(Publication)
admin.site.register(Article)
