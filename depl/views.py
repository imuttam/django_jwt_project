from rest_framework import generics, permissions, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Site
from .serializers import SiteSerializer
from .filters import SiteFilter
from .permissions import CanCreateSite   # if you already created the custom permission

class SiteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [CanCreateSite]   # lists allowed for authenticated; creates limited by permission

    # enable filtering, search, ordering
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]

    # connect the FilterSet
    filterset_class = SiteFilter   # uses your custom SiteFilter

    # fields used by SearchFilter
    search_fields = ['village_site', 'site_id']   # ?search=<term>

    # fields allowed to be used for ordering (whitelist)
    ordering_fields = ['at3_date', 'site_id', 'village_site', 'district', 'lot']
    ordering = ['-at3_date']  # default ordering (optional)


# Retrieve / Update / Delete one site
class SiteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAdminUser]
