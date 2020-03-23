from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from covid19_backend.county.mixins import MixedPermissionsViewSetMixin
from covid19_backend.county.models import County
from covid19_backend.county.serializers import CountySerializer


class CountyView(MixedPermissionsViewSetMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    lookup_field = "ags"
    authentication_classes = [TokenAuthentication]
    permission_classes_by_action = {'create': [IsAuthenticated, IsAdminUser]}

    @swagger_auto_schema(security=[{"api_key": []}])
    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)
