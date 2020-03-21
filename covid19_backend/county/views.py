from rest_framework import viewsets, mixins

from covid19_backend.county.models import County
from covid19_backend.county.serializers import CountySerializer


class CountyView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    lookup_field = "slug"
