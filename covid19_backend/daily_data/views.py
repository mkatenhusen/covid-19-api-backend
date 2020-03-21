from rest_framework import mixins, viewsets

from covid19_backend.daily_data.models import DailyCase, GenderAgeRelation, Gender, Age
from covid19_backend.daily_data.serializers import DailyCaseSerializer, GenderAgeSerializer, GenderSerializer, \
    AgeSerializer


class DailyCasesView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DailyCaseSerializer
    lookup_field = "date_day"

    def get_queryset(self):
        if not self.kwargs:
            queryset = DailyCase.objects.all()
        else:
            queryset = DailyCase.objects.filter(**self.kwargs)
        return queryset


class GenderAgeView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GenderAgeSerializer
    queryset = GenderAgeRelation.objects.all()
    lookup_field = "date_day"


class GenderView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    lookup_field = "genderagerelation__date_day"


class AgeView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = AgeSerializer
    queryset = Age.objects.all()
    lookup_field = "genderagerelation__date_day"
