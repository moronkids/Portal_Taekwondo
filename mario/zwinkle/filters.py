from .models import Collection, PostModel
from django import forms
import django_filters


class kridafilter(django_filters.FilterSet):
    nama = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Collection
        fields = [
            'nama',
        ]


class postfilter(django_filters.FilterSet):
    kategori = django_filters.ModelMultipleChoiceFilter(queryset=PostModel.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = PostModel
        fields = ['kategori',]
