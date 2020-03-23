from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from covid19_backend.county.mixins import MixedPermissionsViewSetMixin
from covid19_backend.daily_data.models import DailyCase, GenderAgeRelation, Gender, Age
from covid19_backend.daily_data.serializers import DailyCaseSerializer, GenderAgeSerializer, GenderSerializer, \
    AgeSerializer


class DailyCasesView(MixedPermissionsViewSetMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = DailyCaseSerializer
    lookup_field = "date_day"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date_day"]
    authentication_classes = [TokenAuthentication]
    permission_classes_by_action = {'create': [IsAuthenticated, IsAdminUser]}

    def get_queryset(self):
        if not self.kwargs:
            queryset = DailyCase.objects.all()
        else:
            queryset = DailyCase.objects.filter(**self.kwargs).order_by("-date_day")
        return queryset

    def get_serializer_context(self):
        return self.kwargs

    @swagger_auto_schema(security=[{"api_key": []}])
    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    @action(detail=False, url_path="latest", methods=["get"])
    def latest(self, request, *args, **kwargs):
        latest_case = DailyCase.objects.filter(**self.kwargs).order_by("-date_day")
        if latest_case:
            serializer = self.get_serializer(latest_case[0], many=False)
            return Response(serializer.data)
        else:
            return Response({})


class GenderAgeView(MixedPermissionsViewSetMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = GenderAgeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date_day"]
    authentication_classes = [TokenAuthentication]
    permission_classes_by_action = {'create': [IsAuthenticated, IsAdminUser]}

    def get_serializer_context(self):
        return self.kwargs

    def get_queryset(self):
        if not self.kwargs:
            queryset = GenderAgeRelation.objects.all()
        else:
            queryset = GenderAgeRelation.objects.filter(**self.kwargs).order_by("-date_day")
        return queryset

    @swagger_auto_schema(security=[{"api_key": []}])
    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    @action(detail=False, url_path="latest", methods=["get"])
    def latest(self, request, *args, **kwargs):
            latest_dates = GenderAgeRelation.objects.only("date_day").filter(**self.kwargs).order_by("-date_day")
            if not latest_dates:
                return Response([])
            latest_gender_age_relations = GenderAgeRelation.objects.filter(**self.kwargs,
                                                                           date_day=latest_dates[0].date_day)
            serializer = self.get_serializer(latest_gender_age_relations, many=True)
            return Response(serializer.data)


# class GenderView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     serializer_class = GenderSerializer
#     queryset = Gender.objects.all()
#     lookup_field = "genderagerelation__date_day"
#
#
# class AgeView(mixins.ListModelMixin, viewsets.GenericViewSet):
#     serializer_class = AgeSerializer
#     queryset = Age.objects.all()
#     lookup_field = "genderagerelation__date_day"
#     filter_backends = [DjangoFilterBackend]
#     filter_class = DayDateFilter
#
#     def get_queryset(self):
#         if not self.kwargs:
#             queryset = Age.objects.all()
#         else:
#             # todo this is an ugly hack
#             temp_dict = {}
#             print(self.kwargs)
#             for (key, value) in self.kwargs.items():
#                 if not key.startswith("genderagerelation__"):
#                     temp_dict["genderagerelation__" + key] = self.kwargs[key]
#                 else:
#                     temp_dict[key] = value
#             queryset = Age.objects.filter(**temp_dict)
#         return queryset
