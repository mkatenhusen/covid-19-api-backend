import django_filters


class DayDateFilter(django_filters.FilterSet):
    date_day = django_filters.DateFilter(method="filter_by_date_day")

    def filter_by_date_day(self, queryset, name, value):
        if value is None:
            return queryset

        return queryset.filter(genderagerelation__date_day=value).distinct()
