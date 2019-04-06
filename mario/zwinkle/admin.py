from django.contrib import admin

# Register your models here.
from .models import buat_login, Publication, Article, PostModel, foto, Collection, CollectionTitle



admin.site.register(buat_login)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(PostModel)
admin.site.register(foto)
admin.site.register(Collection)
admin.site.register(CollectionTitle)


from django.db import models
from django.forms import Textarea

class RulesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }