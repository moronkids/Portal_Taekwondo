from .models import Krida_model
import django_filters


class kridafilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    dojang = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Krida_model
        fields = [
            'name',
            # 'hasilujian',
            'dojang',
        ]
