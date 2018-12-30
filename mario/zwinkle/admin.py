from django.contrib import admin

# Register your models here.
from .models import konten, buat_login, Publication, Article, PostModel


admin.site.register(konten)
admin.site.register(buat_login)
admin.site.register(Publication)
admin.site.register(Article)


from django.db import models
from django.forms import Textarea

class RulesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }