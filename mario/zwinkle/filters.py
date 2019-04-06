from .models import Collection
import django_filters


class kridafilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    dojang = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Collection
        fields = [
            'name',
            # 'hasilujian',
            'dojang',
        ]
