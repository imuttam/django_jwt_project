from django_filters import rest_framework as filters
from .models import DailyReport


class DailyReportFilter(filters.FilterSet):
    
    # Date range filters
    start_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    # Numeric filters (example)
    min_vlr = filters.NumberFilter(field_name="vlr_count", lookup_expr="gte")
    max_vlr = filters.NumberFilter(field_name="vlr_count", lookup_expr="lte")

    min_data_4g = filters.NumberFilter(field_name="data_vol_zte_4g", lookup_expr="gte")
    max_data_4g = filters.NumberFilter(field_name="data_vol_zte_4g", lookup_expr="lte")

    class Meta:
        model = DailyReport
        fields = [
            "start_date", "end_date",
            "min_vlr", "max_vlr",
            "min_data_4g", "max_data_4g",
        ]
