import django_filters
from django_filters import rest_framework as filters
from .models import Site

class SiteFilter(filters.FilterSet):
    # exact matches
    district = filters.CharFilter(field_name='district', lookup_expr='iexact')
    lot = filters.CharFilter(field_name='lot', lookup_expr='iexact')
    village_site = filters.CharFilter(field_name='village_site', lookup_expr='icontains')

    # date range: use from/to query params
    at3_date_from = filters.DateFilter(field_name='at3_date', lookup_expr='gte')
    at3_date_to = filters.DateFilter(field_name='at3_date', lookup_expr='lte')

    class Meta:
        model = Site
        # We define available fields (you can extend this list)
        fields = ['district', 'lot', 'village_site', 'at3_date_from', 'at3_date_to']
