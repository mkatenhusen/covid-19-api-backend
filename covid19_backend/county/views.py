from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from covid19_backend.county.models import County
from covid19_backend.county.serializers import CountySerializer


class CountyView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    lookup_field = "slug"
    authentication_classes = [TokenAuthentication]

    @permission_classes([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)
